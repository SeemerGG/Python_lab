import pandas as pd


def main():
    cont_answer = 0
    file_name = input()
    data = pd.read_csv(file_name, delimiter=',')
    names = data.columns
    for i in range(0,len(data)):
        if(data['Состояние'][i] == 'Завершено'):
            if(data['Тест начат'][i][:13] != data['Завершено'][i][:13]):
                if(data[names[10]][i] == '0,00'):
                    cont_answer += 1;
                if(data[names[11]][i] == '0,00'):
                    cont_answer += 1;
                if(data[names[12]][i] == '0,00'):
                    cont_answer += 1;
    print(cont_answer)

main()