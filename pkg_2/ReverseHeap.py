from TdP_collections.priority_queue.heap_priority_queue import HeapPriorityQueue

class ReverseHeapPriorityQueue(HeapPriorityQueue):

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] > self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)  # recur at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left  # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] > self._data[left]:
                    small_child = right
            if self._data[small_child] > self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)