
import math

class Vector:
    def __init__(self, *components):
        """Initialize a Vector with any number of components."""
        self.components = components

    def __repr__(self):
        """Represent the Vector as a string for output."""
        return f"Vector{self.components}"

    def __add__(self, other):
        """Add two vectors together."""
        self._validate_dimension(other)
        return Vector(*(x + y for x, y in zip(self.components, other.components)))

    def __sub__(self, other):
        """Subtract one vector from another."""
        self._validate_dimension(other)
        return Vector(*(x - y for x, y in zip(self.components, other.components)))

    def __mul__(self, scalar):
        """Multiply the vector by a scalar."""
        if not isinstance(scalar, (int, float)):
            raise TypeError("Scalar must be a number.")
        return Vector(*(x * scalar for x in self.components))

    def __eq__(self, other):
return self.components == other.components


    def dot(self, other):
        """Calculate the dot product of two vectors."""
        self._validate_dimension(other)
        return sum(x * y for x, y in zip(self.components, other.components))

    def magnitude(self):
        """Calculate the magnitude (length) of the vector."""
        return math.sqrt(sum(x**2 for x in self.components))

    def normalize(self):
        """Normalize the vector (make it a unit vector)."""
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return self * (1.0 / magnitude)

    def _validate_dimension(self, other):
        """Private method to validate dimensions of two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be the same dimension.")


class Matrix:
    def __init__(self, rows):
        """Initialize a Matrix from a list of lists."""
        self.rows = rows
        self.validate_matrix()

def _validate_matrix(self):
    """Check if the matrix is well-formed (all rows have the same length)."""
    if len(set(len(row) for row in self.rows)) > 1:
        raise ValueError("All rows must have the same length to form a matrix.")
    def __repr__(self):
        """Represent the Matrix as a string for output."""
        return "\n".join(str(row) for row in self.rows)

    def __add__(self, other):
        """Add two matrices together."""
        self.validate_same_dimension(other)
        return Matrix([[x + y for x, y in zip(row1, row2)] for row1, row2 in zip(self.rows, other.rows)])

    def __mul__(self, other):
        """Multiply matrix by another matrix, a vector or by a scalar."""
        if isinstance(other, Matrix):
            return self.multiply_by_matrix(other)
        elif isinstance(other, (int, float)):
            return self.multiply_by_scalar(other)
        elif isinstance(other, Vector):
            return self.multiply_by_vector(other)
        else:
            raise TypeError("Can only multiply by a scalar, a vector or another matrix.")

    def multiply_by_matrix(self, other):
        """Multiply this matrix by another matrix."""
        if len(self.rows[0]) != len(other.rows):
            raise ValueError("The number of columns in the first matrix must equal the number of rows in the second matrix.")
        other_cols = list(map(list, zip(*other.rows)))  # Transpose other matrix to get columns
        return Matrix([[sum(x * y for x, y in zip(row, col)) for col in other_cols] for row in self.rows])

    def multiply_by_scalar(self, scalar):
        """Multiply this matrix by a scalar."""
        return Matrix([[x * scalar for x in row] for row in self.rows])

    def multiply_by_vector(self, vector):
        """Multiply this matrix by a vector, resulting in another vector."""
        if len(self.rows[0]) != len(vector.components):
            raise ValueError("The number of columns in the matrix must equal the number of components in the vector.")
        return Vector(*[sum(x * y for x, y in zip(row, vector.components)) for row in self.rows])

    def validate_same_dimension(self, other):
        """Check if this matrix has the same dimensions as another matrix."""
        if len(self.rows) != len(other.rows) or len(self.rows[0]) != len(other.rows[0]):
            raise ValueError("Matrices must have the same dimensions to add.")
