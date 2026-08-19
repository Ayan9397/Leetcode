class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        rows = {}

        # Store reserved seats for each affected row
        for row, seat in reservedSeats:
            rows[row] = rows.get(row, 0) | (1 << seat)

        # Rows with no reservations can always accommodate 2 groups
        ans = (n - len(rows)) * 2

        for mask in rows.values():

            # Seats 2,3,4,5
            left = all((mask & (1 << seat)) == 0 for seat in range(2, 6))

            # Seats 6,7,8,9
            right = all((mask & (1 << seat)) == 0 for seat in range(6, 10))

            if left and right:
                # Both groups can fit
                ans += 2

            elif left or right:
                # One of the two outer blocks fits
                ans += 1

            else:
                # Check middle block: 4,5,6,7
                middle = all(
                    (mask & (1 << seat)) == 0
                    for seat in range(4, 8)
                )

                if middle:
                    ans += 1

        return ans