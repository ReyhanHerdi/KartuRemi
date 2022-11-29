def model(kartuS):
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.metrics import accuracy_score

    # Baca file
    poker = pd.read_csv('poker-hand-card-game.csv')

    # Hapus kolom 'Total card
    poker.drop(['Total card'], axis=1, inplace=True)

    # Deklarasi variabel X untuk baris dan y untuk kolom
    X = poker[['Rank of Card 1', 'Rank of Card 2', 'Rank of Card 3', 'Rank of Card 4', 'Rank of Card 5']]
    y = poker['Kategori']


    # Bagi data jadi dua, data train dan data test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=123)


    # Deklarasi model Decision tree
    tree_model = DecisionTreeClassifier() 

    tree_model = tree_model.fit(X_train, y_train)


    # Deklarasi prediksi data
    y_pred = tree_model.predict(X_test)
    
    # Cek akurasi
    acc_secore = round(accuracy_score(y_pred, y_test), 3)
    
    print('Accuracy: ', acc_secore)

    # Coba prediksi
    # print(tree_model.predict([[13, 13, 12, 1, 9]])[0])

    decsAuto = tree_model.predict([kartuS])[0]

    return decsAuto