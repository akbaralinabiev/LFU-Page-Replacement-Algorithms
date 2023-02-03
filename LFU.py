def lfu_algorithm(pages, frame_size):
    frame = []
    page_count = {}
    page_faults = 0
    for page in pages:
        if page not in frame:
            page_faults += 1
            if len(frame) == frame_size:
                frame.pop(frame.index(min(frame, key=lambda x: page_count[x])))
            frame.append(page)
            page_count[page] = 1
        else:
            page_count[page] += 1
    return page_faults

pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
frame_size = 3

print("Number of page faults:", lfu_algorithm(pages, frame_size))
