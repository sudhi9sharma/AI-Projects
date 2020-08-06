import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    links = list(corpus.get(page))
    pages = list(corpus.keys())
    
    values = {}
    
    for page in pages:
        values[page] = (1-damping_factor)/len(pages)
    for link in links:
        values[link] += damping_factor/len(links)
        
    return values


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = list(corpus.keys())
    current_page = random.choice(pages)
    
    samples = {}
    
    for page in pages:
        samples[page] = 0
    for i in range(n):
        values = transition_model(corpus, current_page, damping_factor)
        links = list(values.keys())
        weights = list(values.values())
        current_page = random.choices(links, weights)[0]
        samples[current_page] += 1
        
    for page in pages:
        samples[page] /= SAMPLES
        
    print(round(sum(list(values.values())),10))
    return samples


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pages = list(corpus.keys())
    N = len(pages)
    values  = {}
    for page in pages:
        values[page] = (1/N)
        
    error = 1
    while error > 0.001:
        error = 0
        prev_values = values.copy()
        
        for page in pages:
            i = get_pointing_links(page, corpus)
            a = ((1-damping_factor)/N)
            b= []
            
            for link in i:
                NumLinks = len(corpus.get(link))
                b.append(prev_values[link]/NumLinks)
            values[page] = a + (damping_factor * sum(b))
            new_error = abs(values[page]-prev_values[page])
            
            if error < new_error:
                error = new_error
                
    x = (1-sum(list(values.values())))/N
    for page in pages:
        values[page] += x
    print(round(sum(list(values.values())),10))
    return values

def get_pointing_links(page,corpus):
    i = []
    pages = list(corpus.keys())
    for page_i in pages:
        x_links = list(corpus.get(page_i))
        if page in x_links:
            i.append(page_i)
    return i


if __name__ == "__main__":
    main()
