ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) {
    ListNode *hold_l1 = l1;
    ListNode *hold_l2 = l2;
    while (l1 != nullptr || l2 != nullptr) {
        l1->val += l2->val;
        if (l2->next == nullptr) {
            break;
        }
        l2 = l2->next;
        if (l1->next == nullptr) {
            l1->next = l2;
            break;
        }
        l1 = l1->next;
    }

    l1 = hold_l1;
    while (l1 != nullptr) {
        if (l1->val >= 10) {
            l1->val -= 10;
            if (l1->next == nullptr) {
                l1->next = hold_l2;
                hold_l2->val = 1;
                hold_l2->next = nullptr;
            } else {
                l1->next->val += 1;
            }
        }
        l1 = l1->next;
    }

    return hold_l1;
}
