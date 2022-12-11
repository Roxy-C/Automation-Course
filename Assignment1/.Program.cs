using System;


static void HeapSort(int[] arr) {
	int heapSize = arr.Length;

	for (int i = arr.Length / 2 - 1; i >= 0; i--)
		Heapify(arr, heapSize, i);

	for (int i = arr.Length - 1; i > 0; i--)
	{
		int temp = arr[i];
		arr[i] = arr[0];
		arr[0] = temp;

		Heapify(arr, i, 0);
	}
}

static void Heapify(int[] arr, int heapSize, int index) {
    int left = (index + 1) * 2 - 1;
    int right = (index + 1) * 2;
    int largest = index;

    if (left < heapSize && arr[left] > arr[index])
		largest = left;
	else
		largest = index;

	if (right < heapSize && arr[right] > arr[largest])
		largest = right;

	if (largest != index)
	{
		int temp = arr[index];
		arr[index] = arr[largest];
		arr[largest] = temp;

		Heapify(arr, heapSize, largest);
	}
}



int[] arr = new int[] { 1, 13, -2, 43, -17 };
HeapSort(arr);

foreach (int num in arr) {
	Console.WriteLine(num);
}
