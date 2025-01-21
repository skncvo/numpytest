import numpy as np

#배열 생성
a = np.array([[1,2,3],[4,5,6]])

#행 렬 개수(2,3)
a.shape

#배열의 차원 수 a.ndim == len(a.shape)
a.ndim

#배열에 있는 요소의 개수 a.size == math.prod(a.shape)
a.size

#0으로 된 배열, 1로된 배열, 빈 배열(랜덤값), 순서 배열
np.zeros(3), np.ones(3), np.empty(3), np.arange(4), np.arange(2,7,3)
#지정된 간격으로 선형적 배치 (num = 5면 5개의 요소)
np.linspace(0,10, num = 5)

arr = np.array([2, 1, 5, 3, 7, 4, 6, 8])

#오름차순 정렬
np.sort(arr)

arr2 = np.array([9, 10, 12 ,15 ,11,13])

#배열 합성 np.sort(np.concatenate((arr,arr2)))
np.concatenate((arr,arr2))

array_example = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[0 ,1 ,2, 3],
                           [4, 5, 6, 7]]])

#배열 재구성 1행 6열 -> 3행(세로) 2열(가로) 
arr3 = arr2.reshape(3,2)

#배열 한 차원 늘리기 np.newaxis
arr4 = arr3[np.newaxis, :]

#배열 확장 np.exapnd_dims(배열, axis = 1 or 0) -> 0 == 열, 1 == 행
arr5 = np.expand_dims(arr3, axis = 1)

#조건보다 작은 배열의 인덱스로 배열 생성성
a1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
b1 = np.nonzero(a<5)
#조건 보다 작은 요소 출력력
print(a1[b1]) 

#배열 합성
asum = np.array([1, 1],
                [2, 2])
bsum = np.array([3, 3],
                [4, 4])
#수직합성
np.vstack((asum, bsum))
#수평합성
np.hstack((asum, bsum))