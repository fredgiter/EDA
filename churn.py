{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9e908fb5",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1e41ddf1",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('/Users/charl/Downloads/Churn_Modelling.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c1b23fbf",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>Surname</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>15634602</td>\n",
       "      <td>Hargrave</td>\n",
       "      <td>619</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>2</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101348.88</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>15647311</td>\n",
       "      <td>Hill</td>\n",
       "      <td>608</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>41</td>\n",
       "      <td>1</td>\n",
       "      <td>83807.86</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>112542.58</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>15619304</td>\n",
       "      <td>Onio</td>\n",
       "      <td>502</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>42</td>\n",
       "      <td>8</td>\n",
       "      <td>159660.80</td>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113931.57</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>15701354</td>\n",
       "      <td>Boni</td>\n",
       "      <td>699</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>39</td>\n",
       "      <td>1</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>93826.63</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>15737888</td>\n",
       "      <td>Mitchell</td>\n",
       "      <td>850</td>\n",
       "      <td>Spain</td>\n",
       "      <td>Female</td>\n",
       "      <td>43</td>\n",
       "      <td>2</td>\n",
       "      <td>125510.82</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>79084.10</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   RowNumber  CustomerId   Surname  CreditScore Geography  Gender  Age  \\\n",
       "0          1    15634602  Hargrave          619    France  Female   42   \n",
       "1          2    15647311      Hill          608     Spain  Female   41   \n",
       "2          3    15619304      Onio          502    France  Female   42   \n",
       "3          4    15701354      Boni          699    France  Female   39   \n",
       "4          5    15737888  Mitchell          850     Spain  Female   43   \n",
       "\n",
       "   Tenure    Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
       "0       2       0.00              1          1               1   \n",
       "1       1   83807.86              1          0               1   \n",
       "2       8  159660.80              3          1               0   \n",
       "3       1       0.00              2          0               0   \n",
       "4       2  125510.82              1          1               1   \n",
       "\n",
       "   EstimatedSalary  Exited  \n",
       "0        101348.88       1  \n",
       "1        112542.58       0  \n",
       "2        113931.57       1  \n",
       "3         93826.63       0  \n",
       "4         79084.10       0  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "6185ff79",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "RowNumber          0\n",
       "CustomerId         0\n",
       "Surname            0\n",
       "CreditScore        0\n",
       "Geography          0\n",
       "Gender             0\n",
       "Age                0\n",
       "Tenure             0\n",
       "Balance            0\n",
       "NumOfProducts      0\n",
       "HasCrCard          0\n",
       "IsActiveMember     0\n",
       "EstimatedSalary    0\n",
       "Exited             0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "cb271dae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>Surname</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Geography</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9995</th>\n",
       "      <td>9996</td>\n",
       "      <td>15606229</td>\n",
       "      <td>Obijiaku</td>\n",
       "      <td>771</td>\n",
       "      <td>France</td>\n",
       "      <td>Male</td>\n",
       "      <td>39</td>\n",
       "      <td>5</td>\n",
       "      <td>0.00</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>96270.64</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9996</th>\n",
       "      <td>9997</td>\n",
       "      <td>15569892</td>\n",
       "      <td>Johnstone</td>\n",
       "      <td>516</td>\n",
       "      <td>France</td>\n",
       "      <td>Male</td>\n",
       "      <td>35</td>\n",
       "      <td>10</td>\n",
       "      <td>57369.61</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>101699.77</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9997</th>\n",
       "      <td>9998</td>\n",
       "      <td>15584532</td>\n",
       "      <td>Liu</td>\n",
       "      <td>709</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>36</td>\n",
       "      <td>7</td>\n",
       "      <td>0.00</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>42085.58</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9998</th>\n",
       "      <td>9999</td>\n",
       "      <td>15682355</td>\n",
       "      <td>Sabbatini</td>\n",
       "      <td>772</td>\n",
       "      <td>Germany</td>\n",
       "      <td>Male</td>\n",
       "      <td>42</td>\n",
       "      <td>3</td>\n",
       "      <td>75075.31</td>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>92888.52</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9999</th>\n",
       "      <td>10000</td>\n",
       "      <td>15628319</td>\n",
       "      <td>Walker</td>\n",
       "      <td>792</td>\n",
       "      <td>France</td>\n",
       "      <td>Female</td>\n",
       "      <td>28</td>\n",
       "      <td>4</td>\n",
       "      <td>130142.79</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>38190.78</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      RowNumber  CustomerId    Surname  CreditScore Geography  Gender  Age  \\\n",
       "9995       9996    15606229   Obijiaku          771    France    Male   39   \n",
       "9996       9997    15569892  Johnstone          516    France    Male   35   \n",
       "9997       9998    15584532        Liu          709    France  Female   36   \n",
       "9998       9999    15682355  Sabbatini          772   Germany    Male   42   \n",
       "9999      10000    15628319     Walker          792    France  Female   28   \n",
       "\n",
       "      Tenure    Balance  NumOfProducts  HasCrCard  IsActiveMember  \\\n",
       "9995       5       0.00              2          1               0   \n",
       "9996      10   57369.61              1          1               1   \n",
       "9997       7       0.00              1          0               1   \n",
       "9998       3   75075.31              2          1               0   \n",
       "9999       4  130142.79              1          1               0   \n",
       "\n",
       "      EstimatedSalary  Exited  \n",
       "9995         96270.64       0  \n",
       "9996        101699.77       0  \n",
       "9997         42085.58       1  \n",
       "9998         92888.52       1  \n",
       "9999         38190.78       0  "
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.tail()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "ab87766c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>RowNumber</th>\n",
       "      <th>CustomerId</th>\n",
       "      <th>CreditScore</th>\n",
       "      <th>Age</th>\n",
       "      <th>Tenure</th>\n",
       "      <th>Balance</th>\n",
       "      <th>NumOfProducts</th>\n",
       "      <th>HasCrCard</th>\n",
       "      <th>IsActiveMember</th>\n",
       "      <th>EstimatedSalary</th>\n",
       "      <th>Exited</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>10000.00000</td>\n",
       "      <td>1.000000e+04</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.00000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "      <td>10000.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>5000.50000</td>\n",
       "      <td>1.569094e+07</td>\n",
       "      <td>650.528800</td>\n",
       "      <td>38.921800</td>\n",
       "      <td>5.012800</td>\n",
       "      <td>76485.889288</td>\n",
       "      <td>1.530200</td>\n",
       "      <td>0.70550</td>\n",
       "      <td>0.515100</td>\n",
       "      <td>100090.239881</td>\n",
       "      <td>0.203700</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>2886.89568</td>\n",
       "      <td>7.193619e+04</td>\n",
       "      <td>96.653299</td>\n",
       "      <td>10.487806</td>\n",
       "      <td>2.892174</td>\n",
       "      <td>62397.405202</td>\n",
       "      <td>0.581654</td>\n",
       "      <td>0.45584</td>\n",
       "      <td>0.499797</td>\n",
       "      <td>57510.492818</td>\n",
       "      <td>0.402769</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.00000</td>\n",
       "      <td>1.556570e+07</td>\n",
       "      <td>350.000000</td>\n",
       "      <td>18.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>11.580000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>2500.75000</td>\n",
       "      <td>1.562853e+07</td>\n",
       "      <td>584.000000</td>\n",
       "      <td>32.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.00000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>51002.110000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>5000.50000</td>\n",
       "      <td>1.569074e+07</td>\n",
       "      <td>652.000000</td>\n",
       "      <td>37.000000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>97198.540000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>100193.915000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>7500.25000</td>\n",
       "      <td>1.575323e+07</td>\n",
       "      <td>718.000000</td>\n",
       "      <td>44.000000</td>\n",
       "      <td>7.000000</td>\n",
       "      <td>127644.240000</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>149388.247500</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>10000.00000</td>\n",
       "      <td>1.581569e+07</td>\n",
       "      <td>850.000000</td>\n",
       "      <td>92.000000</td>\n",
       "      <td>10.000000</td>\n",
       "      <td>250898.090000</td>\n",
       "      <td>4.000000</td>\n",
       "      <td>1.00000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>199992.480000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         RowNumber    CustomerId   CreditScore           Age        Tenure  \\\n",
       "count  10000.00000  1.000000e+04  10000.000000  10000.000000  10000.000000   \n",
       "mean    5000.50000  1.569094e+07    650.528800     38.921800      5.012800   \n",
       "std     2886.89568  7.193619e+04     96.653299     10.487806      2.892174   \n",
       "min        1.00000  1.556570e+07    350.000000     18.000000      0.000000   \n",
       "25%     2500.75000  1.562853e+07    584.000000     32.000000      3.000000   \n",
       "50%     5000.50000  1.569074e+07    652.000000     37.000000      5.000000   \n",
       "75%     7500.25000  1.575323e+07    718.000000     44.000000      7.000000   \n",
       "max    10000.00000  1.581569e+07    850.000000     92.000000     10.000000   \n",
       "\n",
       "             Balance  NumOfProducts    HasCrCard  IsActiveMember  \\\n",
       "count   10000.000000   10000.000000  10000.00000    10000.000000   \n",
       "mean    76485.889288       1.530200      0.70550        0.515100   \n",
       "std     62397.405202       0.581654      0.45584        0.499797   \n",
       "min         0.000000       1.000000      0.00000        0.000000   \n",
       "25%         0.000000       1.000000      0.00000        0.000000   \n",
       "50%     97198.540000       1.000000      1.00000        1.000000   \n",
       "75%    127644.240000       2.000000      1.00000        1.000000   \n",
       "max    250898.090000       4.000000      1.00000        1.000000   \n",
       "\n",
       "       EstimatedSalary        Exited  \n",
       "count     10000.000000  10000.000000  \n",
       "mean     100090.239881      0.203700  \n",
       "std       57510.492818      0.402769  \n",
       "min          11.580000      0.000000  \n",
       "25%       51002.110000      0.000000  \n",
       "50%      100193.915000      0.000000  \n",
       "75%      149388.247500      0.000000  \n",
       "max      199992.480000      1.000000  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "246e597f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(10000, 14)"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "5282e6a6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1080x576 with 12 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "\n",
    "df.hist(bins=50, color='blue', figsize=(15, 8))\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "911ef80b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance',\n",
       "       'NumOfProducts', 'HasCrCard', 'IsActiveMember', 'EstimatedSalary',\n",
       "       'Exited'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1, inplace=True)\n",
    "df.columns        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "63a03d43",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 10000 entries, 0 to 9999\n",
      "Data columns (total 11 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   CreditScore      10000 non-null  int64  \n",
      " 1   Geography        10000 non-null  object \n",
      " 2   Gender           10000 non-null  object \n",
      " 3   Age              10000 non-null  int64  \n",
      " 4   Tenure           10000 non-null  int64  \n",
      " 5   Balance          10000 non-null  float64\n",
      " 6   NumOfProducts    10000 non-null  int64  \n",
      " 7   HasCrCard        10000 non-null  int64  \n",
      " 8   IsActiveMember   10000 non-null  int64  \n",
      " 9   EstimatedSalary  10000 non-null  float64\n",
      " 10  Exited           10000 non-null  int64  \n",
      "dtypes: float64(2), int64(7), object(2)\n",
      "memory usage: 859.5+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "b207c564",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'sns' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [12]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m fig, ax \u001b[38;5;241m=\u001b[39m plt\u001b[38;5;241m.\u001b[39msubplots(figsize\u001b[38;5;241m=\u001b[39m(\u001b[38;5;241m6\u001b[39m, \u001b[38;5;241m6\u001b[39m))\n\u001b[1;32m----> 3\u001b[0m \u001b[43msns\u001b[49m\u001b[38;5;241m.\u001b[39mcountplot(x\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mExited\u001b[39m\u001b[38;5;124m'\u001b[39m, data\u001b[38;5;241m=\u001b[39mtrain_df, palette\u001b[38;5;241m=\u001b[39mcolors, ax\u001b[38;5;241m=\u001b[39max)\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m index, value \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28menumerate\u001b[39m(train_df[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mExited\u001b[39m\u001b[38;5;124m'\u001b[39m]\u001b[38;5;241m.\u001b[39mvalue_counts()):\n\u001b[0;32m      6\u001b[0m     label \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;241m.\u001b[39mformat(\u001b[38;5;28mround\u001b[39m((value \u001b[38;5;241m/\u001b[39m train_df[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mExited\u001b[39m\u001b[38;5;124m'\u001b[39m]\u001b[38;5;241m.\u001b[39mshape[\u001b[38;5;241m0\u001b[39m]) \u001b[38;5;241m*\u001b[39m \u001b[38;5;241m100\u001b[39m, \u001b[38;5;241m2\u001b[39m))\n",
      "\u001b[1;31mNameError\u001b[0m: name 'sns' is not defined"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(figsize=(6, 6))\n",
    " \n",
    "sns.countplot(x='Exited', data=train_df, palette=colors, ax=ax)\n",
    " \n",
    "for index, value in enumerate(train_df['Exited'].value_counts()):\n",
    "    label = '{}%'.format(round((value / train_df['Exited'].shape[0]) * 100, 2))\n",
    "    ax.annotate(label,\n",
    "                xy=(index, value + 250),\n",
    "                ha='center',\n",
    "                va='center',\n",
    "                color=colors[index],\n",
    "                fontweight='bold',\n",
    "                size=font_size + 4)\n",
    " \n",
    "ax.set_xticklabels(['Retained', 'Churned'])\n",
    "ax.set_xlabel('Status')\n",
    "ax.set_ylabel('Count')\n",
    "ax.set_ylim([0, 7000]);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "2cc090a9",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "2b3c26de",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'train_df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [14]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m fig, ax \u001b[38;5;241m=\u001b[39m plt\u001b[38;5;241m.\u001b[39msubplots(figsize\u001b[38;5;241m=\u001b[39m(\u001b[38;5;241m6\u001b[39m, \u001b[38;5;241m6\u001b[39m))\n\u001b[1;32m----> 3\u001b[0m sns\u001b[38;5;241m.\u001b[39mcountplot(x\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mExited\u001b[39m\u001b[38;5;124m'\u001b[39m, data\u001b[38;5;241m=\u001b[39m\u001b[43mtrain_df\u001b[49m, palette\u001b[38;5;241m=\u001b[39mcolors, ax\u001b[38;5;241m=\u001b[39max)\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m index, value \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28menumerate\u001b[39m(train_df[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mExited\u001b[39m\u001b[38;5;124m'\u001b[39m]\u001b[38;5;241m.\u001b[39mvalue_counts()):\n\u001b[0;32m      6\u001b[0m     label \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;241m.\u001b[39mformat(\u001b[38;5;28mround\u001b[39m((value \u001b[38;5;241m/\u001b[39m train_df[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mExited\u001b[39m\u001b[38;5;124m'\u001b[39m]\u001b[38;5;241m.\u001b[39mshape[\u001b[38;5;241m0\u001b[39m]) \u001b[38;5;241m*\u001b[39m \u001b[38;5;241m100\u001b[39m, \u001b[38;5;241m2\u001b[39m))\n",
      "\u001b[1;31mNameError\u001b[0m: name 'train_df' is not defined"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(figsize=(6, 6))\n",
    " \n",
    "sns.countplot(x='Exited', data=train_df, palette=colors, ax=ax)\n",
    " \n",
    "for index, value in enumerate(train_df['Exited'].value_counts()):\n",
    "    label = '{}%'.format(round((value / train_df['Exited'].shape[0]) * 100, 2))\n",
    "    ax.annotate(label,\n",
    "                xy=(index, value + 250),\n",
    "                ha='center',\n",
    "                va='center',\n",
    "                color=colors[index],\n",
    "                fontweight='bold',\n",
    "                size=font_size + 4)\n",
    " \n",
    "ax.set_xticklabels(['Retained', 'Churned'])\n",
    "ax.set_xlabel('Status')\n",
    "ax.set_ylabel('Count')\n",
    "ax.set_ylim([0, 7000]);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "80d6f600",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import confusion_matrix, accuracy_score, precision_score , recall_score, f1_score, roc_curve, auc\n",
    "from sklearn.multiclass import OneVsRestClassifier"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "a9b4f22a",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'train_df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [16]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m fig, ax \u001b[38;5;241m=\u001b[39m plt\u001b[38;5;241m.\u001b[39msubplots(figsize\u001b[38;5;241m=\u001b[39m(\u001b[38;5;241m6\u001b[39m, \u001b[38;5;241m6\u001b[39m))\n\u001b[1;32m----> 3\u001b[0m sns\u001b[38;5;241m.\u001b[39mcountplot(x\u001b[38;5;241m=\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mExited\u001b[39m\u001b[38;5;124m'\u001b[39m, data\u001b[38;5;241m=\u001b[39m\u001b[43mtrain_df\u001b[49m, palette\u001b[38;5;241m=\u001b[39mcolors, ax\u001b[38;5;241m=\u001b[39max)\n\u001b[0;32m      5\u001b[0m \u001b[38;5;28;01mfor\u001b[39;00m index, value \u001b[38;5;129;01min\u001b[39;00m \u001b[38;5;28menumerate\u001b[39m(train_df[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mExited\u001b[39m\u001b[38;5;124m'\u001b[39m]\u001b[38;5;241m.\u001b[39mvalue_counts()):\n\u001b[0;32m      6\u001b[0m     label \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m'\u001b[39m\u001b[38;5;132;01m{}\u001b[39;00m\u001b[38;5;124m%\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;241m.\u001b[39mformat(\u001b[38;5;28mround\u001b[39m((value \u001b[38;5;241m/\u001b[39m train_df[\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mExited\u001b[39m\u001b[38;5;124m'\u001b[39m]\u001b[38;5;241m.\u001b[39mshape[\u001b[38;5;241m0\u001b[39m]) \u001b[38;5;241m*\u001b[39m \u001b[38;5;241m100\u001b[39m, \u001b[38;5;241m2\u001b[39m))\n",
      "\u001b[1;31mNameError\u001b[0m: name 'train_df' is not defined"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXwAAAFpCAYAAACf/JPiAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAAAPDUlEQVR4nO3cX4jld3nH8c/TXQP1T42YVWz+YFqicS9M0TFK0TZWWpP0IgheJIrSICyhRrw0FKoX3tSLgojRZQlBvDEXNWgs0VAo1kKaNhPQaJTINtJkGyEbFQsKDRufXszUHcZJ5uzMmdk4z+sFA/P7ne/MPPNl9p1ffjPnVHcHgIPvd873AADsD8EHGELwAYYQfIAhBB9gCMEHGGLb4FfVnVX1VFV97zker6r6TFWdrKqHq+pNyx8TgN1a5Ar/C0mufZ7Hr0tyxfrbsSSf3/1YACzbtsHv7m8l+enzLLkhyRd7zQNJLqyq1yxrQACWYxn38C9O8sSG41Pr5wB4ATm8hM9RW5zb8vUaqupY1m775CUvecmbr7zyyiV8eYA5Hnrooae7+8hOPnYZwT+V5NINx5ckeXKrhd19IsmJJFlZWenV1dUlfHmAOarqv3b6scu4pXNPkg+u/7XO25L8vLt/vITPC8ASbXuFX1VfSnJNkouq6lSSTyR5UZJ09/Ek9ya5PsnJJL9McvNeDQvAzm0b/O6+aZvHO8mHlzYRAHvCM20BhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYYqHgV9W1VfVoVZ2sqtu2ePzlVfW1qvpOVT1SVTcvf1QAdmPb4FfVoSS3J7kuydEkN1XV0U3LPpzk+919VZJrkvx9VV2w5FkB2IVFrvCvTnKyux/r7meS3JXkhk1rOsnLqqqSvDTJT5OcWeqkAOzKIsG/OMkTG45PrZ/b6LNJ3pDkySTfTfLR7v7VUiYEYCkWCX5tca43Hb87ybeT/H6SP0ry2ar6vd/4RFXHqmq1qlZPnz59jqMCsBuLBP9Ukks3HF+StSv5jW5OcnevOZnkR0mu3PyJuvtEd69098qRI0d2OjMAO7BI8B9MckVVXb7+i9gbk9yzac3jSd6VJFX16iSvT/LYMgcFYHcOb7egu89U1a1J7ktyKMmd3f1IVd2y/vjxJJ9M8oWq+m7WbgF9rLuf3sO5AThH2wY/Sbr73iT3bjp3fMP7Tyb5i+WOBsAyeaYtwBCCDzCE4AMMIfgAQwg+wBCCDzCE4AMMIfgAQwg+wBCCDzCE4AMMIfgAQwg+wBCCDzCE4AMMIfgAQwg+wBCCDzCE4AMMIfgAQwg+wBCCDzCE4AMMIfgAQwg+wBCCDzCE4AMMIfgAQwg+wBCCDzCE4AMMIfgAQwg+wBCCDzCE4AMMIfgAQwg+wBCCDzCE4AMMIfgAQwg+wBCCDzCE4AMMIfgAQwg+wBCCDzCE4AMMIfgAQwg+wBCCDzCE4AMMIfgAQwg+wBCCDzCE4AMMIfgAQwg+wBALBb+qrq2qR6vqZFXd9hxrrqmqb1fVI1X1L8sdE4DdOrzdgqo6lOT2JH+e5FSSB6vqnu7+/oY1Fyb5XJJru/vxqnrVHs0LwA4tcoV/dZKT3f1Ydz+T5K4kN2xa874kd3f340nS3U8td0wAdmuR4F+c5IkNx6fWz230uiSvqKpvVtVDVfXBrT5RVR2rqtWqWj19+vTOJgZgRxYJfm1xrjcdH07y5iR/meTdSf62ql73Gx/UfaK7V7p75ciRI+c8LAA7t+09/Kxd0V+64fiSJE9usebp7v5Fkl9U1beSXJXkh0uZEoBdW+QK/8EkV1TV5VV1QZIbk9yzac1Xk7yjqg5X1YuTvDXJD5Y7KgC7se0Vfnefqapbk9yX5FCSO7v7kaq6Zf3x4939g6r6RpKHk/wqyR3d/b29HByAc1Pdm2/H74+VlZVeXV09L18b4LdVVT3U3Ss7+VjPtAUYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2CIhYJfVddW1aNVdbKqbnuedW+pqmer6r3LGxGAZdg2+FV1KMntSa5LcjTJTVV19DnWfSrJfcseEoDdW+QK/+okJ7v7se5+JsldSW7YYt1Hknw5yVNLnA+AJVkk+BcneWLD8an1c79WVRcneU+S48/3iarqWFWtVtXq6dOnz3VWAHZhkeDXFud60/Gnk3ysu599vk/U3Se6e6W7V44cObLgiAAsw+EF1pxKcumG40uSPLlpzUqSu6oqSS5Kcn1VnenuryxjSAB2b5HgP5jkiqq6PMl/J7kxyfs2Lujuy////ar6QpJ/FHuAF5Ztg9/dZ6rq1qz99c2hJHd29yNVdcv648973x6AF4ZFrvDT3fcmuXfTuS1D391/tfuxAFg2z7QFGELwAYYQfIAhBB9gCMEHGELwAYYQfIAhBB9gCMEHGELwAYYQfIAhBB9gCMEHGELwAYYQfIAhBB9gCMEHGELwAYYQfIAhBB9gCMEHGELwAYYQfIAhBB9gCMEHGELwAYYQfIAhBB9gCMEHGELwAYYQfIAhBB9gCMEHGELwAYYQfIAhBB9gCMEHGELwAYYQfIAhBB9gCMEHGELwAYYQfIAhBB9gCMEHGELwAYYQfIAhBB9gCMEHGELwAYYQfIAhBB9gCMEHGELwAYYQfIAhBB9giIWCX1XXVtWjVXWyqm7b4vH3V9XD62/3V9VVyx8VgN3YNvhVdSjJ7UmuS3I0yU1VdXTTsh8l+dPufmOSTyY5sexBAdidRa7wr05ysrsf6+5nktyV5IaNC7r7/u7+2frhA0kuWe6YAOzWIsG/OMkTG45PrZ97Lh9K8vXdDAXA8h1eYE1tca63XFj1zqwF/+3P8fixJMeS5LLLLltwRACWYZEr/FNJLt1wfEmSJzcvqqo3JrkjyQ3d/ZOtPlF3n+jule5eOXLkyE7mBWCHFgn+g0muqKrLq+qCJDcmuWfjgqq6LMndST7Q3T9c/pgA7Na2t3S6+0xV3ZrkviSHktzZ3Y9U1S3rjx9P8vEkr0zyuapKkjPdvbJ3YwNwrqp7y9vxe25lZaVXV1fPy9cG+G1VVQ/t9ILaM20BhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYQvABhhB8gCEEH2AIwQcYYqHgV9W1VfVoVZ2sqtu2eLyq6jPrjz9cVW9a/qgA7Ma2wa+qQ0luT3JdkqNJbqqqo5uWXZfkivW3Y0k+v+Q5AdilRa7wr05ysrsf6+5nktyV5IZNa25I8sVe80CSC6vqNUueFYBdWCT4Fyd5YsPxqfVz57oGgPPo8AJraotzvYM1qapjWbvlkyT/W1XfW+DrT3BRkqfP9xAvEPbiLHtxlr046/U7/cBFgn8qyaUbji9J8uQO1qS7TyQ5kSRVtdrdK+c07QFlL86yF2fZi7PsxVlVtbrTj13kls6DSa6oqsur6oIkNya5Z9Oae5J8cP2vdd6W5Ofd/eOdDgXA8m17hd/dZ6rq1iT3JTmU5M7ufqSqbll//HiSe5Ncn+Rkkl8muXnvRgZgJxa5pZPuvjdrUd947viG9zvJh8/xa584x/UHmb04y16cZS/Oshdn7Xgvaq3VABx0XloBYIg9D76XZThrgb14//oePFxV91fVVedjzv2w3V5sWPeWqnq2qt67n/Ptp0X2oqquqapvV9UjVfUv+z3jflng38jLq+prVfWd9b04kL8vrKo7q+qp5/rT9R13s7v37C1rv+T9zyR/kOSCJN9JcnTTmuuTfD1rf8v/tiT/vpczna+3Bffij5O8Yv396ybvxYZ1/5y13x+993zPfR5/Li5M8v0kl60fv+p8z30e9+Jvknxq/f0jSX6a5ILzPfse7MWfJHlTku89x+M76uZeX+F7WYaztt2L7r6/u3+2fvhA1p7PcBAt8nORJB9J8uUkT+3ncPtskb14X5K7u/vxJOnug7ofi+xFJ3lZVVWSl2Yt+Gf2d8y9193fytr39lx21M29Dr6XZTjrXL/PD2Xtv+AH0bZ7UVUXJ3lPkuM52Bb5uXhdkldU1Ter6qGq+uC+Tbe/FtmLzyZ5Q9ae2PndJB/t7l/tz3gvKDvq5kJ/lrkLS3tZhgNg4e+zqt6ZteC/fU8nOn8W2YtPJ/lYdz+7djF3YC2yF4eTvDnJu5L8bpJ/q6oHuvuHez3cPltkL96d5NtJ/izJHyb5p6r61+7+nz2e7YVmR93c6+Av7WUZDoCFvs+qemOSO5Jc190/2afZ9tsie7GS5K712F+U5PqqOtPdX9mXCffPov9Gnu7uXyT5RVV9K8lVSQ5a8BfZi5uT/F2v3cg+WVU/SnJlkv/YnxFfMHbUzb2+peNlGc7adi+q6rIkdyf5wAG8etto273o7su7+7Xd/dok/5Dkrw9g7JPF/o18Nck7qupwVb04yVuT/GCf59wPi+zF41n7P51U1auz9kJij+3rlC8MO+rmnl7ht5dl+LUF9+LjSV6Z5HPrV7Zn+gC+YNSCezHCInvR3T+oqm8keTjJr5Lc0d0H7pVmF/y5+GSSL1TVd7N2W+Nj3X3gXkWzqr6U5JokF1XVqSSfSPKiZHfd9ExbgCE80xZgCMEHGELwAYYQfIAhBB9gCMEHGELwAYYQfIAh/g91XH0oS0ZTvgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 432x432 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(figsize=(6, 6))\n",
    " \n",
    "sns.countplot(x='Exited', data=train_df, palette=colors, ax=ax)\n",
    " \n",
    "for index, value in enumerate(train_df['Exited'].value_counts()):\n",
    "    label = '{}%'.format(round((value / train_df['Exited'].shape[0]) * 100, 2))\n",
    "    ax.annotate(label,\n",
    "                xy=(index, value + 250),\n",
    "                ha='center',\n",
    "                va='center',\n",
    "                color=colors[index],\n",
    "                fontweight='bold',\n",
    "                size=font_size + 4)\n",
    " \n",
    "ax.set_xticklabels(['Retained', 'Churned'])\n",
    "ax.set_xlabel('Status')\n",
    "ax.set_ylabel('Count')\n",
    "ax.set_ylim([0, 7000]);"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "9cd561bc",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df.select_dtypes(exclude=[\"object\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "892126bf",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Establish target feature, churn\n",
    "y = df.Exited.values\n",
    "# Drop the target feature from remaining features\n",
    "X = df.drop('Exited', axis = 1)\n",
    "# Save dataframe column titles to list, we will need them in next step\n",
    "cols = X.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "9148c5b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "LogisticRegression(C=1000000000000.0, fit_intercept=False, solver='liblinear')"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Import the necessary sklearn method\n",
    "from sklearn.preprocessing import MinMaxScaler\n",
    "# Instantiate a Min-Max scaling object\n",
    "mm = MinMaxScaler()\n",
    "# Fit and transform our feature data into a pandas dataframe\n",
    "X = pd.DataFrame(mm.fit_transform(X))\n",
    "#Split the data into training and testing sets:\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .25, random_state = 33)\n",
    "# Instantiate a logistic regression model without an intercept, arbitrarily large C value will offset the lack of intercept\n",
    "logreg = LogisticRegression(fit_intercept = False, C = 1e12, solver = 'liblinear')\n",
    "# Fit the model to our X and y training sets\n",
    "logreg.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "bc957f43",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'np' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Input \u001b[1;32mIn [21]\u001b[0m, in \u001b[0;36m<cell line: 4>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      2\u001b[0m y_hat_test \u001b[38;5;241m=\u001b[39m logreg\u001b[38;5;241m.\u001b[39mpredict(X_test)\n\u001b[0;32m      3\u001b[0m \u001b[38;5;66;03m# Find residual differences between train data and predicted train data\u001b[39;00m\n\u001b[1;32m----> 4\u001b[0m residuals \u001b[38;5;241m=\u001b[39m \u001b[43mnp\u001b[49m\u001b[38;5;241m.\u001b[39mabs(y_train, y_hat_train)\n\u001b[0;32m      7\u001b[0m \u001b[38;5;66;03m# Print the number of times our model was correct ('0') and incorrect ('1')\u001b[39;00m\n\u001b[0;32m      8\u001b[0m \u001b[38;5;28mprint\u001b[39m(pd\u001b[38;5;241m.\u001b[39mSeries(residuals)\u001b[38;5;241m.\u001b[39mvalue_counts())\n",
      "\u001b[1;31mNameError\u001b[0m: name 'np' is not defined"
     ]
    }
   ],
   "source": [
    "y_hat_train = logreg.predict(X_train)\n",
    "y_hat_test = logreg.predict(X_test)\n",
    "# Find residual differences between train data and predicted train data\n",
    "residuals = np.abs(y_train, y_hat_train)\n",
    "\n",
    "\n",
    "# Print the number of times our model was correct ('0') and incorrect ('1')\n",
    "print(pd.Series(residuals).value_counts())\n",
    "      \n",
    "# Print normalized amount of times our model was correct (percentage)\n",
    "print(pd.Series(residuals).value_counts(normalize = True))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "75b7d272",
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "81a0133e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0    5944\n",
      "1    1556\n",
      "dtype: int64\n",
      "0    0.792533\n",
      "1    0.207467\n",
      "dtype: float64\n"
     ]
    }
   ],
   "source": [
    "y_hat_train = logreg.predict(X_train)\n",
    "y_hat_test = logreg.predict(X_test)\n",
    "# Find residual differences between train data and predicted train data\n",
    "residuals = np.abs(y_train, y_hat_train)\n",
    "\n",
    "\n",
    "# Print the number of times our model was correct ('0') and incorrect ('1')\n",
    "print(pd.Series(residuals).value_counts())\n",
    "      \n",
    "# Print normalized amount of times our model was correct (percentage)\n",
    "print(pd.Series(residuals).value_counts(normalize = True))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "db1855bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Pass actual test and predicted target test outcomes to function\n",
    "cnf_matrix = confusion_matrix(y_test, y_hat_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "bfc21ee5",
   "metadata": {},
   "outputs": [],
   "source": [
    "precision_train = precision_score(y_train, y_hat_train)\n",
    "precision_test = precision_score(y_test, y_hat_test)\n",
    "recall_train = recall_score(y_train, y_hat_train)\n",
    "recall_test = recall_score(y_test, y_hat_test)\n",
    "accuracy_train = accuracy_score(y_train, y_hat_train)\n",
    "accuracy_test = accuracy_score(y_test, y_hat_test)\n",
    "f1_train = f1_score(y_train, y_hat_train)\n",
    "f1_test = f1_score(y_test, y_hat_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "3b0cbc00",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "([<matplotlib.axis.YTick at 0x11bc29e1f40>,\n",
       "  <matplotlib.axis.YTick at 0x11bc29e1df0>,\n",
       "  <matplotlib.axis.YTick at 0x11bc29e1310>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a2ccd0>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a08dc0>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a32310>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a3a370>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a3aac0>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a40250>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a409d0>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a3abb0>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a237f0>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a40520>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a4a550>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a4aca0>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a4f430>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a4fb80>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a4a520>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a3a0d0>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a56040>,\n",
       "  <matplotlib.axis.YTick at 0x11bc2a56700>],\n",
       " [Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, ''),\n",
       "  Text(0, 0, '')])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Calculate probability score of each point in training set\n",
    "y_train_score = logreg.decision_function(X_train)\n",
    "# Calculate false positive rate(fpr), true pos. rate (tpr), and thresholds for train set\n",
    "train_fpr, train_tpr, train_thresholds = roc_curve(y_train, y_hat_train)\n",
    "# Calculate probability score of each point in test set\n",
    "y_test_score = logreg.decision_function(X_test)\n",
    "# Calculate fpr, tpr, and thresholds for test set\n",
    "test_fpr, test_tpr, test_thresholds = roc_curve(y_test, y_hat_test)\n",
    "\n",
    "# Plot the training FPR and TPR\n",
    "plt.plot(train_fpr, train_tpr, label = 'Precision-Recall curve')\n",
    "# Plot positive sloped 1:1 line for reference\n",
    "plt.plot([0,1],[0,1])\n",
    "plt.xlim([0.0, 1.0])\n",
    "plt.ylim([0.0, 1.05])\n",
    "plt.xticks([i/20.0 for i in range(21)])\n",
    "plt.yticks([i/20.0 for i in range(21)])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1036e69c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
