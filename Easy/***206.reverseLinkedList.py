class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next # temp variable
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

        # base case: if the list is empty or has only one element, return it
        if head is None or head.next is None:
            return head
        
        # recursive case: reverse the rest of the list and append the current node to the end
        new_head = reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
        
