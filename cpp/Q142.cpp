ListNode *detectCycle(ListNode *head) {
    vector<ListNode *> nxtptr;
    ListNode *holdhead = head;

    int dangercount = 0;
    while (head != nullptr) {
        if (head->next == holdhead) {
            return head->next;
        }
        if (head->next == nullptr) {
            return head->next;
        }
        for (int i = 0; i < nxtptr.size(); i++) {
            if (head->next == nxtptr[i]) {
                return head->next;
            }
        }
        nxtptr.push_back(head->next);
        head = head->next;
        dangercount += 1;
        if (dangercount >= 2000) {
            cout << "dangers memory access happened." << endl;
            break;
        }
    }


    return nullptr;
}
