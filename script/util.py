import numpy as np

def arb_linear_interp(x: np.array,
                      y: np.array,
                      resolution: np.array,
                      data: np.array):
    x_grid = np.array([]).astype(int)
    y_grid = np.array([]).astype(int)
    # check data length consistency before interpolation:
    if len(x)==len(y):
        if len(resolution) == (len(x)-1):
            # sort x, y to make an open path
            np.sort(x)
            np.sort(y)

            for p in range(len(resolution)):
                x_grid = np.append(x_grid, np.linspace(x[p], x[p+1], resolution[p]).astype(int))
                y_grid = np.append(y_grid, np.linspace(y[p], y[p+1], resolution[p]).astype(int))
        else:
            raise ValueError(f'Length of resolution should be {len(x)}, but got {len(resolution)}')
    else:
        raise ValueError('Interpolation path should have save number of nodes on 2 axes.')

    # calculate distance from origin along the interpolation path
    path = np.sqrt(np.square(x_grid-x_grid[0]) + np.square(y_grid-y_grid[0]))
    return path, data[x_grid, y_grid]
