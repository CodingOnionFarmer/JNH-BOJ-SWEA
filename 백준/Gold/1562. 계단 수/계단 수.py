end08 = end09 = end4 = end5 = 1
end17 = end26 = end35 = end18 = end27 = end36 = end45 = end19 = end28 = end37 = end46 = e18 = e27 = e36 = e45 = 2
for _ in range(int(input()) - 1):
    end08, end17, end26, end35, end4 = end17, end08 + end26, end17 + end35, end26 + 2 * end4, end35
    end09, end18, end27, end36, end45 = end18, end09 + end27, end18 + end36, end27 + end45, end36 + end45
    end19, end28, end37, end46, end5 = end28, end19 + end37, end28 + end46, end37 + 2 * end5, end46
    e18, e27, e36, e45 = e27, e18 + e36, e27 + e45, e36 + e45

# print(end09 + end18 + end27 + end36 + end45)
# print(e18 + e27 + e36 + e45)
# print(- end08 - end17 - end26 - end35 - end4)
# print(- end19 - end28 - end37 - end46 - end5)
print((end09 + end18 + end27 + end36 + end45 + e18 + e27 + e36 + e45 - end08 - end17 - end26 - end35 - end4 - end19 - end28 - end37 - end46 - end5) % (10 ** 9))
