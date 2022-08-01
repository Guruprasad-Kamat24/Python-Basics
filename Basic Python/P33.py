def main():
    input_string =input()
    user_list = input_string.split(',')
    for i in range(len(user_list)):
        user_list[i] = int(user_list[i])
        res = []
    for ele in user_list:
        res.append(ele + ele)
    print (str(res))
    return(0)
if __name__=="__main__":
    main()