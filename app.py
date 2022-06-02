import streamlit as st
from matplotlib import pyplot as plt
import pre_processing
import numpy as np

col1, col2 = st.columns(2)
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/en/5/52/National_Institutional_Ranking_Framework_logo.png")
with col2:
    st.header("National Institutional Ranking Framework Analysis")
st.markdown("---")
st.subheader("Select the year")
col1, col2, col3 = st.columns(3)
with col1:
    button1 = st.button("Year 2019")
with col2:
    button2 = st.button("Year 2020")
with col3:
    button3 = st.button("Year 2021")
st.markdown("---")

if button1:
    df_2019, top5 = pre_processing.read_2019()
    st.title("Top 5 Engineering colleges 2019")
    col1, col2,col3,col4,col5 = st.columns(5)

    with col1:
        st.image(pre_processing.logo[top5[0]])
        st.caption(top5[0])
    with col2:
        st.image(pre_processing.logo[top5[1]])
        st.caption(top5[1])
    with col3:
        st.image(pre_processing.logo[top5[2]])
        st.caption(top5[2])
    with col4:
        st.image(pre_processing.logo[top5[3]])
        st.caption(top5[3])
    with col5:
        st.image(pre_processing.logo[top5[4]])
        st.caption(top5[4])

    st.markdown("---")
    st.write("NIRF 2019 data")
    st.dataframe(df_2019)
    st.markdown("---")

    st.write("plot for the No. of Male Students, No. of Female Students and Total Students")
    fig = plt.figure(figsize=(10, 5))
    x = np.arange(1, 101)
    ax = plt.subplot(111)
    ax.bar(x - 0.4, df_2019.iloc[:, 3], width=0.4, color='b', align='center')
    ax.bar(x + 0.4, df_2019.iloc[:, 4], width=0.4, color='g', align='center')
    plt.legend(['No. of MaleStudents', 'No. of Female Students', 'Total Students'])
    plt.xlabel('Rank of Collage according to NIRF 2019 ranking')
    plt.ylabel('No. of students')
    plt.title('Bar chart')
    st.pyplot(fig)

    st.markdown("---")
    st.write("Histogram of frequency of No. of students receiving full tuition fee reimbursement from the Private Bodies.")
    fig = plt.figure(figsize=(10, 5))
    plt.hist(df_2019['No. of students receiving full tuition fee reimbursement from the Private Bodies'])
    plt.xlabel('No. of students receiving full tuition fee reimbursement from the Private Bodies')
    plt.ylabel('frequency')
    plt.title('Histogram')
    st.pyplot(fig)

    st.markdown("---")
    st.write("No. of students who are not receiving full tuition fee reimbursement")
    fig = plt.figure(figsize=(10, 5))
    plt.plot(np.arange(1, 101), df_2019.iloc[:, 11], color='r', marker='o')
    plt.xlabel('Rank of the college')
    plt.ylabel('No. of students who are not receiving full tuition fee reimbursement')
    plt.title('Line Graph')
    st.pyplot(fig)

    st.markdown("---")
    st.write("A scatter plot of Outside Country (Including male & female)")
    fig = plt.figure(figsize=(10, 5))
    plt.scatter(np.arange(1, 101), df_2019.iloc[:, 4])
    plt.title('Scatter Plot')
    plt.xlabel('Rank of the collage')
    plt.ylabel('Outside Country (Including male & female)')
    st.pyplot(fig)

    st.markdown("---")
    st.write("A plot of Within State (Including male & female), Outside State (Including male & female), Outside Country (Including male & female), and Total Students")
    fig = plt.figure(figsize=(10, 5))
    plt.plot(np.arange(1, 101), df_2019.iloc[:, 3], color='Blue', marker='o')
    plt.plot(np.arange(1, 101), df_2019.iloc[:, 4], color='Red', marker='o')
    plt.plot(np.arange(1, 101), df_2019.iloc[:, 5], color='Green', marker='o')
    plt.legend(['Within State (Including male & female)', 'Outside State (Including male & female)',
                'Outside Country (Including male & female)'])
    plt.xlabel('Rank of Collage according to NIRF 2019 ranking')
    plt.ylabel('No. of students')
    plt.title('Line chart')
    st.pyplot(fig)

    st.markdown("---")
    st.write("No. of Male Students vs. No. of Female Students")
    fig = plt.figure(figsize=(10, 5))
    x = [df_2019['No. of MaleStudents'].sum(), df_2019['No. of Female Students'].sum()]
    label = ['Male', 'Female']
    plt.pie(x=x, labels=label, autopct='%1.3f%%')
    plt.title('total male and female students of all 100 colleges')
    st.pyplot(fig)

    st.markdown("---")
    st.write("Oldest colleges of India")
    top_15 = pre_processing.Top_15()
    st.dataframe(top_15)
    st.markdown("---")

    st.write("Different colleges according to year of establishment")
    fig = plt.figure(figsize=(10, 5))
    plt.bar(top_15['S_name'], top_15['Age'], width=0.5)
    plt.xlabel('Name of the institute')
    plt.xticks(rotation=90)
    plt.ylabel('Years')
    plt.title('Bar plot')
    st.pyplot(fig)

    st.write("created by Ronak Pandya")

if button2:
    df_2020, top5 = pre_processing.read_2020()
    st.title("Top 5 Engineering colleges 2020")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(pre_processing.logo[top5[0]])
        st.caption(top5[0])
    with col2:
        st.image(pre_processing.logo[top5[1]])
        st.caption(top5[1])
    with col3:
        st.image(pre_processing.logo[top5[2]])
        st.caption(top5[2])
    with col4:
        st.image(pre_processing.logo[top5[3]])
        st.caption(top5[3])
    with col5:
        st.image(pre_processing.logo[top5[4]])
        st.caption(top5[4])

    st.markdown("---")
    st.write("NIRF 2020 data")
    st.dataframe(df_2020)
    st.markdown("---")

    fig = plt.figure(figsize=(10, 5))
    st.write("plot for the No. of Male Students, No. of Female Students and Total Students")
    x = np.arange(1, 101)
    ax = plt.subplot(111)
    ax.bar(x - 0.4, df_2020.iloc[:, 3], width=0.4, color='b', align='center')
    ax.bar(x + 0.4, df_2020.iloc[:, 4], width=0.4, color='g', align='center')
    plt.legend(['No. of MaleStudents', 'No. of Female Students', 'Total Students'])
    plt.xlabel('Rank of Collage according to NIRF 2020 ranking')
    plt.ylabel('No. of students')
    plt.title('Bar chart')
    st.pyplot(fig)

    st.markdown("---")
    st.write("Histogram of frequency of No. of students receiving full tuition fee reimbursement from the Private Bodies.")
    fig = plt.figure(figsize=(10, 5))
    plt.hist(df_2020['No. of students receiving full tuition fee reimbursement from the Private Bodies'])
    plt.xlabel('No. of students receiving full tuition fee reimbursement from the Private Bodies')
    plt.ylabel('frequency')
    plt.title('Histogram')
    st.pyplot(fig)

    st.markdown("---")
    fig = plt.figure(figsize=(10, 5))

    st.write("No. of students who are not receiving full tuition fee reimbursement")
    plt.plot(np.arange(1, 101), df_2020.iloc[:, 11], color='r', marker='o')
    plt.xlabel('Rank of the college')
    plt.ylabel('No. of students who are not receiving full tuition fee reimbursement')
    plt.title('Line Graph')
    st.pyplot(fig)

    st.markdown("---")
    fig = plt.figure(figsize=(10, 5))
    st.write("A scatter plot of Outside Country (Including male & female)")

    plt.scatter(np.arange(1, 101), df_2020.iloc[:, 4])
    plt.title('Scatter Plot')
    plt.xlabel('Rank of the collage')
    plt.ylabel('Outside Country (Including male & female)')
    st.pyplot(fig)

    st.markdown("---")
    fig = plt.figure(figsize=(10, 5))
    st.write(
        "A plot of Within State (Including male & female), Outside State (Including male & female), Outside Country (Including male & female), and Total Students")
    plt.plot(np.arange(1, 101), df_2020.iloc[:, 3], color='Blue', marker='o')
    plt.plot(np.arange(1, 101), df_2020.iloc[:, 4], color='Red', marker='o')
    plt.plot(np.arange(1, 101), df_2020.iloc[:, 5], color='Green', marker='o')
    plt.legend(['Within State (Including male & female)', 'Outside State (Including male & female)',
                'Outside Country (Including male & female)'])
    plt.xlabel('Rank of Collage according to NIRF 2020 ranking')
    plt.ylabel('No. of students')
    plt.title('Line chart')
    st.pyplot(fig)

    st.markdown("---")
    fig = plt.figure(figsize=(10, 5))
    st.write("No. of Male Students vs. No. of Female Students")
    x = [df_2020['No. of MaleStudents'].sum(), df_2020['No. of Female Students'].sum()]
    label = ['Male', 'Female']
    plt.pie(x=x, labels=label, autopct='%1.3f%%')
    plt.title('total male and female students of all 100 colleges')
    st.pyplot(fig)

    st.markdown("---")
    st.write("Oldest colleges of India")
    top_15 = pre_processing.Top_15()
    st.dataframe(top_15)
    st.markdown("---")

    st.write("Different colleges according to year of establishment")
    fig = plt.figure(figsize=(10, 5))
    plt.bar(top_15['S_name'], top_15['Age'], width=0.5)
    plt.xlabel('Name of the institute')
    plt.xticks(rotation=90)
    plt.ylabel('Years')
    plt.title('Bar plot')
    st.pyplot(fig)

    st.write("created by Ronak Pandya")

if button3:
    df_2021, top5 = pre_processing.read_2021()
    st.title("Top 5 Engineering colleges 2021")
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.image(pre_processing.logo[top5[0]])
        st.caption(top5[0])
    with col2:
        st.image(pre_processing.logo[top5[1]])
        st.caption(top5[1])
    with col3:
        st.image(pre_processing.logo[top5[2]])
        st.caption(top5[2])
    with col4:
        st.image(pre_processing.logo[top5[3]])
        st.caption(top5[3])
    with col5:
        st.image(pre_processing.logo[top5[4]])
        st.caption(top5[4])

    st.markdown("---")
    st.write("NIRF 2021 data")
    st.dataframe(df_2021)
    st.markdown("---")

    fig = plt.figure(figsize=(10, 5))
    st.write("plot for the No. of Male Students, No. of Female Students and Total Students")
    x = np.arange(1, 101)
    ax = plt.subplot(111)
    ax.bar(x - 0.4, df_2021.iloc[:, 3], width=0.4, color='b', align='center')
    ax.bar(x + 0.4, df_2021.iloc[:, 4], width=0.4, color='g', align='center')
    plt.legend(['No. of MaleStudents', 'No. of Female Students', 'Total Students'])
    plt.xlabel('Rank of Collage according to NIRF 2021 ranking')
    plt.ylabel('No. of students')
    plt.title('Bar chart')
    st.pyplot(fig)

    st.markdown("---")
    st.write("Histogram of frequency of No. of students receiving full tuition fee reimbursement from the Private Bodies.")
    fig = plt.figure(figsize=(10, 5))
    plt.hist(df_2021['No. of students receiving full tuition fee reimbursement from the Private Bodies'])
    plt.xlabel('No. of students receiving full tuition fee reimbursement from the Private Bodies')
    plt.ylabel('frequency')
    plt.title('Histogram')
    st.pyplot(fig)

    st.markdown("---")
    fig = plt.figure(figsize=(10, 5))
    st.write("No. of students who are not receiving full tuition fee reimbursement")
    plt.plot(np.arange(1, 101), df_2021.iloc[:, 11], color='r', marker='o')
    plt.xlabel('Rank of the college')
    plt.ylabel('No. of students who are not receiving full tuition fee reimbursement')
    plt.title('Line Graph')
    st.pyplot(fig)

    st.markdown("---")
    fig = plt.figure(figsize=(10, 5))
    st.write("A scatter plot of Outside Country (Including male & female)")
    plt.scatter(np.arange(1, 101), df_2021.iloc[:, 4])
    plt.title('Scatter Plot')
    plt.xlabel('Rank of the collage')
    plt.ylabel('Outside Country (Including male & female)')
    st.pyplot(fig)

    st.markdown("---")
    fig = plt.figure(figsize=(10, 5))
    st.write("A plot of Within State (Including male & female), Outside State (Including male & female), Outside Country (Including male & female), and Total Students")
    plt.plot(np.arange(1, 101), df_2021.iloc[:, 3], color='Blue', marker='o')
    plt.plot(np.arange(1, 101), df_2021.iloc[:, 4], color='Red', marker='o')
    plt.plot(np.arange(1, 101), df_2021.iloc[:, 5], color='Green', marker='o')
    plt.legend(['Within State (Including male & female)', 'Outside State (Including male & female)',
                'Outside Country (Including male & female)'])
    plt.xlabel('Rank of Collage according to NIRF 2021 ranking')
    plt.ylabel('No. of students')
    plt.title('Line chart')
    st.pyplot(fig)

    st.markdown("---")
    fig = plt.figure(figsize=(10, 5))
    st.write("No. of Male Students vs. No. of Female Students")
    x = [df_2021['No. of MaleStudents'].sum(), df_2021['No. of Female Students'].sum()]
    label = ['Male', 'Female']
    plt.pie(x=x, labels=label, autopct='%1.3f%%')
    plt.title('total male and female students of all 100 colleges')
    st.pyplot(fig)

    st.markdown("---")
    st.write("Oldest colleges of India")
    top_15 = pre_processing.Top_15()
    st.dataframe(top_15)
    st.markdown("---")

    st.write("Different colleges according to year of establishment")
    fig = plt.figure(figsize=(10, 5))
    plt.bar(top_15['S_name'], top_15['Age'], width=0.5)
    plt.xlabel('Name of the institute')
    plt.xticks(rotation=90)
    plt.ylabel('Years')
    plt.title('Bar plot')
    st.pyplot(fig)

    st.write("created by Ronak Pandya")











