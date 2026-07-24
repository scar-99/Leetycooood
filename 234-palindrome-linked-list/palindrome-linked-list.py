
class Solution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True

        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow
        while curr:

            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        n = head
        m = prev

        while m:
            if n.val != m.val:
                return False
            n = n.next
            m = m.next
        return True