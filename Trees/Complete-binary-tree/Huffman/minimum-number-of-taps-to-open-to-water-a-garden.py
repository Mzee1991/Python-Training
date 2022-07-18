class Solution:
    def minTaps(self, n, ranges):
        taps = 0

        # # Save the right-most possible jump for each left most index
        jumps = [-1]*(n)
        for idx, num in enumerate(ranges):
            if num == 0:
                continue
            left_most = max(0, idx-num)
            right_most = min(n, idx+num)

            jumps[left_most] = max(jumps[left_most], right_most)

        # # Jump Game II
        current_jump_end = 0
        furthest_can_reach = -1  # furthest jump we made/could have made
        for idx, right_most in enumerate(jumps):

            # we continuously find the how far we can reach in the current jump
            # record the futhest point accessible in our current jump
            furthest_can_reach = max(right_most, furthest_can_reach)

            # if we have come to the end of the current jump, we need to make another jump
            # the new  jump should start immediately after the old jump
            if idx == current_jump_end:
                # if we cannot make a jump and we need to make a jump to increase the furthest_can_reach
                if right_most == -1 and furthest_can_reach <= idx:
                    return -1
                # move to the furthest possible point
                current_jump_end = furthest_can_reach
                taps += 1

        if furthest_can_reach == n:
            return taps
        return -1
