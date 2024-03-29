from CheckHameln import check_hameln
from GetHameln import get_hameln

def main():
    # 更新情報を取得
    novels = check_hameln()

    # 更新情報を元に小説を取得
    for novel in novels:
        get_hameln(novel)

if __name__ == '__main__':
    main()