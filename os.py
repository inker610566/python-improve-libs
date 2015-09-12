import os

def sorted_walk(rootpath):
    # report this
    dirpath, dirs, files = next(os.walk(rootpath))
    yield (dirpath, dirs, files)
    for ndir in sorted(dirs):
        ndirpath = os.path.join(rootpath, ndir)
        for _, ndirs, nfiles in sorted_walk(ndirpath):
            yield (ndirpath, ndirs, nfiles)

