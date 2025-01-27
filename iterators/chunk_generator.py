def chunk_generator(iterable, chunk_size):
    itr = iter(iterable)

    try:
        while True:
            chunk = []
            for _ in range(chunk_size):
                chunk.append(next(itr))
            yield chunk
    except StopIteration:
        if chunk:
            yield chunk


for chunk in chunk_generator([1, 2, 3, 4, 5], 2):
    print(chunk)

