from math import *
import streamlit as st

st.title("Kombinatorikk")
st.divider()
st.write("Denne webappen er basert på dei fire tellemåtane i kombinatorikk")

#st.logo("https://www.oisteing.com/images/logowww.png", link="https://www.oisteing.com")

st.logo("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSXL74BGleH6oFgRBkKovXDFNTb0h5U46mhnQ&s", link="https://www.oisteing.com")


def ordna_uten(n,r):
    return(int(factorial(n)/factorial(n-r)))

def ordna_med(n,r):
    return(int(n**r))

def uordna_uten(n,r):
    return(int(factorial(n)/(factorial(n-r)*factorial(r))))


def uordna_med(n,k):
    return(int(factorial(n+k-1)/(factorial(n-1)*factorial(k))))



st.write("1: Ordna utvalg uten tilbakelegging")
st.write("2: Ordna utvalg med tilbakelegging")
st.write("3: Uordna utvalg uten tilbakelegging")
st.write("4: Uordna utvalg med tilbakelegging")

valg = int(st.number_input("Hva vil du gjøre? (1 - 4): ", value=1, max_value=4, min_value=1))
a=b=1

if valg==1:
    st.write("Du har valgt 1... Ordna utvalg uten tilbakelegging. Skriv inn n og så r")
    a=int(st.number_input("n: ", value=1, min_value=b))
    b=int(st.number_input("r: ",  min_value=1, max_value=a))
    st.write(" Det er totalt ",ordna_uten(a,b), "mulige utvalg.")

if valg==2:
    st.write("Du har valgt 2... Ordna utvalg med tilbakelegging. Skriv inn n og så r")
    a=int(st.number_input("n: ", value=1, min_value=1))
    b=int(st.number_input("r: ", value=1, min_value=1))
    st.write(" Det er totalt ",ordna_med(a,b), "mulige utvalg.")

if valg==3:
    st.write("Du har valgt 3... Uordna utvalg uten tilbakelegging. Skriv inn n og så r")
    a=int(st.number_input("n: ", value=1, min_value=1))
    b=int(st.number_input("r: ", value=1, min_value=1))
    st.write(" Det er totalt ",uordna_uten(a,b), "mulige utvalg.")

if valg==4:
    st.write("Du har valgt 4... Uordna utvalg med tilbakelegging. Skriv inn n og så r")
    a=int(st.number_input("n: ", value=1, min_value=1))
    b=int(st.number_input("r: ", value=1, min_value=1))
    st.write(" Det er totalt ",uordna_med(a,b), "mulige utvalg.")
