import numpy as np
print(f"Using numpy version {np.version.version}")

if __name__ == "__main__":
    oned = np.array([1, 2, 3, 4, 5])
    twod = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    print(oned.ndim)
    print(twod.ndim)

    fived = np.array([1, 2, 3], ndmin=5)
    print(fived)
    print(fived.ndim)

    chars = np.array(["1", "2"])
    print(chars)

    mixed = np.array([1, "2"])
    print(mixed)