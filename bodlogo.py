# 1. b
# 2. b
# 3. b
# 4. a
# 5. c
# 6. a
# 7.1 c
# 7.2   !!!!!
# 8. c
# 9. a
# 10. d
# 11. b
# 12. a
# 13.  Массив нь санах ойн зэргэлдээ байрлалд хадгалагдсан элементүүдийн цуглуулга юм.
#  Энэ нь индексийг ашиглан элементүүдэд хурдан хандах боломжийг олгодог. Массивууд нь тогтмол хэмжээтэй тул санах ойн хуваарилалт
#   нь эмхэтгэх үед хийгддэг бөгөөд ажиллах үед өөрчлөгдөх боломжгүй.

# linked list-ийн хувьд node бүр нь өгөгдөл болон дарааллын дараагийн зангилааны reference ( pointer/заагч) агуулсан 
# node-ны цуглуулга. Linked list нь динамик хэмжээтэй бөгөөд санах ойг ажиллах үед хуваарилж, уян хатан санах ой ашиглах
#  боломжийг олгодог.

# 14. Стек ба мод нь компьютерийн шинжлэх ухаанд хэрэглэгддэг хоёр үндсэн өгөгдлийн бүтэц боловч тэдгээр нь тэс өөр зорилготой бөгөөд ялгаатай шинж 
# чанартай байдаг.
# Стек: Стек нь LIFO зарчмыг баримталдаг шугаман өгөгдлийн бүтэц юм. Үүнийг овоолсон хавтан шиг төсөөлөөд үзэж болно: 
#  зөвхөн дээд хавтанг авч, дээр нь таваг нэмэх гэх мэтээр дээрээсээ нэмэгдэж эсвэл хасагдж ажиллана..
# Хэрэглээ нь Стекийг програмчлалд функцийн дуудлагын менежментэд ихээхэн ашигладаг. Функцийг дуудах үед түүний гүйцэтгэлийн 
# контекст стек рүү түлхэгдэнэ. Энэ нь буцаж ирэхэд контекст нь стекээс гарч ирнэ.

# Мод: Мод нь зангилаа бүрээс бүрдэх шаталсан өгөгдлийн бүтэц бөгөөд зангилаа бүр нь өөрийн гэсэн утгатай бөгөөд түүний хүүхдүүдийн reference-tай 
# байдаг. Модыг ихэвчлэн шаталсан харилцааг илэрхийлэхэд ашигладаг.
# Хэрэглээ нь Модыг файлын систем, байгууллагын бүтэц, XML/HTML баримт зэрэг шаталсан харилцаатай өгөгдлийг төлөөлөхөд ашигладаг.
# Хоёртын хайлтын мод (BST): Модыг хурдан өгөгдөл хайх, оруулах, устгахад ашигладаг. BST нь зангилаа бүрийн хувьд түүний зүүн дэд модны бүх элементүүд бага,
# баруун дэд модны бүх элементүүд илүү том байхыг баталгаажуулдаг.
# Tries (Угтгал мод): Эдгээр нь толь бичигт түгээмэл байдаг мөрүүдийг үр дүнтэй хайх, эрэмбэлэх, автоматаар бөглөх функцүүдэд ашиглагддаг.
# 15. c
# 16. a
# 17. b 
# 18. c
# 19-22

# 1. greedy algorithm
# def zoos(niit):
#     zoos = [25, 10, 5, 1]  
#     result = {} 
    
#     for i in zoos:
#         count = niit // i  
#         if count > 0:
#             result[i] = count  
#             niit -= count * i  
#     return result

# niit = 83
# result = zoos(niit)
# for zoos, count in result.items():
#     print(f"{count}*{zoos} dollars")

# asuult1 - 67 = 2*25, 1*10, 1*5, 2*1
# asuult2 - c. merge sort

# 2. huffman coding
# class Node:
#     def __init__(self, char, freq):
#         self.char = char
#         self.freq = freq
#         self.left = None
#         self.right = None

# def build_huffman(frequencies):
#     nodes = [Node(char,freq) for char,freq in frequencies.items()]
#     # nodes
#     while len(nodes) > 1:
#         nodes.sort(key=lambda x:x.freq)
#         right = nodes[1]
#         left = nodes[0]
#         merge = Node(None,right.freq + left.freq)
#         merge.left = left
#         merge.right = right
#         nodes = nodes[2:] + [merge]
#     return nodes[0]

# def generate(node, prefix='', code={}):
#     if node is not None:
#         if node.char is not None:
#             code[node.char]=prefix
#         generate(node.left, prefix +'0', code)
#         generate(node.right, prefix +'1', code)
#     return code
# frequencies = {
#     'd': 4,
#     'e': 3,
#     'a': 10,
#     'b': 15,
#     'c': 6,
#     'f': 4
# }
# root = build_huffman(frequencies)
# x = generate(root)
# for char in sorted(frequencies):
#     print(f"{char}: {x[char]}")

# # 3. algorithm completion 
# asuult1 - b

# 4 binary search tree/\

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinarySearchTree:
#     def __init__(self):
#         self.root = None

#     def insert(self, value):
#         def _insert(node, value):
#             if not node:
#                 return Node(value)
#             if value < node.value:
#                 node.left = _insert(node.left, value)
#             else:
#                 node.right = _insert(node.right, value)
#             return node
        
#         self.root = _insert(self.root, value)

#     def search(self, value):
#         def _search(node, value):
#             if not node:
#                 return False
#             if node.value == value:
#                 return True
#             elif value < node.value:
#                 return _search(node.left, value)
#             else:
#                 return _search(node.right, value)

#         return _search(self.root, value)

#     def find_min(self):
#         def _find_min(node):
#             current = node
#             while current and current.left:
#                 current = current.left
#             return current

#         min_node = _find_min(self.root)
#         return min_node.value if min_node else None

#     def find_max(self):
#         def _find_max(node):
#             current = node
#             while current and current.right:
#                 current = current.right
#             return current

#         max_node = _find_max(self.root)
#         return max_node.value if max_node else None

# bst = BinarySearchTree()
# values = [20, 9, 25, 5, 12, 15, 30]
# for value in values:
#     bst.insert(value)

# print("Search:", bst.search(12))   
# print("Search:", bst.search(7))     
# print("Minimum value:", bst.find_min())  
# print("Maximum value:", bst.find_max()) 

bubble sort insertion sort
# ##Insertion_sort algorithm
# # def insertion_sort(arr):
# #     for i in range(1, len(arr)):
# #         baga = arr[i]
# #         j = i - 1
# #         while j>=0 and baga < arr[j]:
# #             arr[j+1] = arr[j]
# #             j-=1
# #         arr[j+1]=baga
# #     return arr
# # sorted_arr = insertion_sort([51,12,65,52,19,89])
# # print(sorted_arr)



# ##Bubble sort algorithm
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         baga = arr[i]
#         for j in range(i+1, len(arr)):
#             if baga > arr[j]:
#                 baga = arr[j]
#                 j+=1
#     return arr 
# sorted_arr = bubble_sort([51,12,65,52,19,89])
# print(sorted_arr)
