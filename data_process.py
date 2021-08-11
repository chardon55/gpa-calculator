import pandas as pd


def main():
    df = pd.read_csv('./score.csv')

    new_table = {
        "score": [],
        "weight": [],
    }

    for i, row in df.iterrows():
        new_table['score'].append(row['score1'])
        new_table['score'].append(row['score2'])
        new_table['weight'].append(row['weight1'])
        new_table['weight'].append(row['weight2'])

    with open('score1.csv', 'w+') as f:
        f.write(pd.DataFrame(new_table).to_csv())


if __name__ == '__main__':
    main()
