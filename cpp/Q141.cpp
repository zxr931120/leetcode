bool hasCycle(ListNode *head) {
    if (head == nullptr) {
        return false;
    }
    ListNode *ptr1 = head;
    ListNode *ptr2 = head;
    if (ptr1->next == nullptr) {
        return false;
    }
    ptr1 = ptr1->next;
    ptr2 = ptr2->next;
    ptr2 = ptr2->next;

    while (ptr2 != nullptr) {
        if (ptr2 == ptr1) {
            return true;
        }

        ptr2 = ptr2->next;
        if (ptr2 == nullptr) {
            return false;
        }
        if (ptr2 == ptr1) {
            return true;
        }
        ptr2 = ptr2->next;
        ptr1 = ptr1->next;
    }

    return false;

}
