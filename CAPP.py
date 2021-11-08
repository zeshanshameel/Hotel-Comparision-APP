import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("finalf.csv")

st.title("Hotel Comparision APP")

hotel_names = ['Ocean Palms Goa','Silver Sands Serenity','Goa Woodlands Hotel','The Byke Old Anchor Beach Resort & Spa',
'Whispering Palms Beach Resort','Rivasa Resort','Rendezvous Beach Resort','Hotel Campal','Hotel MR Manfred']

hotel1 = st.selectbox("select Hotel 1",hotel_names)
hotel1 = df[df['Hotel']==hotel1]

hotel2 = st.selectbox("select Hotel 2",hotel_names)
hotel2 = df[df['Hotel']==hotel2]


if st.button("Compare"):

    #all the features in a list
    polfeatlis = list(hotel1['feature'])

    #all the features in a list
    polfeatlis1 = list(hotel2['feature'])

    #common features from hotel 1 and hotel 2
    commonfeat = list(set.intersection(set(polfeatlis), set(polfeatlis1)))

    # appending the pos values of common features from hotel 1
    a = []
    for i in commonfeat:
        a.append(float(hotel1['pos%'].loc[hotel1['feature'] == i]))

    # appending the pos values of common features from hotel 2
    b = []
    for i in commonfeat:
        b.append(float(hotel2['pos%'].loc[hotel2['feature'] == i]))

    # appending the pos values of common features from hotel 1
    a1 = []
    for i in commonfeat:
        a1.append(float(hotel1['neg%'].loc[hotel1['feature'] == i]))

    # appending the pos values of common features from hotel 2
    b1 = []
    for i in commonfeat:
        b1.append(float(hotel2['neg%'].loc[hotel2['feature'] == i]))
    
    N = len(a)

    # Position of bars on x-axis
    ind = np.arange(N)

    # Figure size
    plt.figure(figsize=(20,10))

    # Width of a bar 
    width = 0.3       

    # Plotting
    plt.bar(ind, a , width, label='Hotel1 POS')
    plt.bar(ind,a1,width,label = 'Hotel1 NEG')
    plt.bar(ind + width, b, width, label='Hotel2 POS')
    plt.bar(ind+width,b1,width,label='Hotel2 NEG')

    plt.xlabel('common features')
    plt.ylabel('Polarity')
    plt.title('polarity comparision')

    # xticks()
    # First argument - A list of positions at which ticks should be placed
    # Second argument -  A list of labels to place at the given locations
    plt.xticks(ind + width / 2, commonfeat)

    # Finding the best position for legends and putting it
    plt.legend(loc='best')
    st.pyplot()
    st.set_option('deprecation.showPyplotGlobalUse', False)

    #feature present only on hotel 1
    onlypolfeat = list(set(polfeatlis).difference(set(polfeatlis1)))
    #feature present only on hotel 2
    onlypolfeat1 = list(set(polfeatlis1).difference(set(polfeatlis)))
    # appending the pos values of features present only on hotel 1
    opp = []
    for i in onlypolfeat:
        opp.append(float(hotel1['pos%'].loc[hotel1['feature'] == i]))

    opn = []
    for i in onlypolfeat:
        opn.append(float(hotel1['neg%'].loc[hotel1['feature'] == i]))

    opp1 = []
    for i in onlypolfeat1:
        opp1.append(float(hotel2['pos%'].loc[hotel2['feature'] == i]))

    opn1 = []
    for i in onlypolfeat1:
        opn1.append(float(hotel2['neg%'].loc[hotel2['feature'] == i]))

    plt.figure(figsize=(20,10))
    plt.bar(onlypolfeat,opp,label = np.unique(hotel1['Hotel']))
    plt.bar(onlypolfeat1,opp1,label = 'only 2nd hotel')
    plt.xlabel('features')
    plt.ylabel('Polarity')
    plt.title('polarity comparision')
    plt.legend(loc='best')
    st.pyplot()
