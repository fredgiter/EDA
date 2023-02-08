{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e6b755c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "20a5ffdc",
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
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>bmi</th>\n",
       "      <th>children</th>\n",
       "      <th>smoker</th>\n",
       "      <th>region</th>\n",
       "      <th>charges</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19</td>\n",
       "      <td>female</td>\n",
       "      <td>27.900</td>\n",
       "      <td>0</td>\n",
       "      <td>yes</td>\n",
       "      <td>southwest</td>\n",
       "      <td>16884.92400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>18</td>\n",
       "      <td>male</td>\n",
       "      <td>33.770</td>\n",
       "      <td>1</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>1725.55230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>28</td>\n",
       "      <td>male</td>\n",
       "      <td>33.000</td>\n",
       "      <td>3</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>4449.46200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>33</td>\n",
       "      <td>male</td>\n",
       "      <td>22.705</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>21984.47061</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>32</td>\n",
       "      <td>male</td>\n",
       "      <td>28.880</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>3866.85520</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age     sex     bmi  children smoker     region      charges\n",
       "0   19  female  27.900         0    yes  southwest  16884.92400\n",
       "1   18    male  33.770         1     no  southeast   1725.55230\n",
       "2   28    male  33.000         3     no  southeast   4449.46200\n",
       "3   33    male  22.705         0     no  northwest  21984.47061\n",
       "4   32    male  28.880         0     no  northwest   3866.85520"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv('/Users/charl/Downloads/insurance.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2068604a",
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
       "      <th>age</th>\n",
       "      <th>sex</th>\n",
       "      <th>bmi</th>\n",
       "      <th>children</th>\n",
       "      <th>smoker</th>\n",
       "      <th>region</th>\n",
       "      <th>charges</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>19</td>\n",
       "      <td>female</td>\n",
       "      <td>27.900</td>\n",
       "      <td>0</td>\n",
       "      <td>yes</td>\n",
       "      <td>southwest</td>\n",
       "      <td>16884.92400</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>18</td>\n",
       "      <td>male</td>\n",
       "      <td>33.770</td>\n",
       "      <td>1</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>1725.55230</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>28</td>\n",
       "      <td>male</td>\n",
       "      <td>33.000</td>\n",
       "      <td>3</td>\n",
       "      <td>no</td>\n",
       "      <td>southeast</td>\n",
       "      <td>4449.46200</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>33</td>\n",
       "      <td>male</td>\n",
       "      <td>22.705</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>21984.47061</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>32</td>\n",
       "      <td>male</td>\n",
       "      <td>28.880</td>\n",
       "      <td>0</td>\n",
       "      <td>no</td>\n",
       "      <td>northwest</td>\n",
       "      <td>3866.85520</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   age     sex     bmi  children smoker     region      charges\n",
       "0   19  female  27.900         0    yes  southwest  16884.92400\n",
       "1   18    male  33.770         1     no  southeast   1725.55230\n",
       "2   28    male  33.000         3     no  southeast   4449.46200\n",
       "3   33    male  22.705         0     no  northwest  21984.47061\n",
       "4   32    male  28.880         0     no  northwest   3866.85520"
      ]
     },
     "execution_count": 6,
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
   "execution_count": 8,
   "id": "db6ef579",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 1338 entries, 0 to 1337\n",
      "Data columns (total 7 columns):\n",
      " #   Column    Non-Null Count  Dtype  \n",
      "---  ------    --------------  -----  \n",
      " 0   age       1338 non-null   int64  \n",
      " 1   sex       1338 non-null   object \n",
      " 2   bmi       1338 non-null   float64\n",
      " 3   children  1338 non-null   int64  \n",
      " 4   smoker    1338 non-null   object \n",
      " 5   region    1338 non-null   object \n",
      " 6   charges   1338 non-null   float64\n",
      "dtypes: float64(2), int64(2), object(3)\n",
      "memory usage: 73.3+ KB\n"
     ]
    }
   ],
   "source": [
    "df.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "913f6353",
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
       "      <th>age</th>\n",
       "      <th>bmi</th>\n",
       "      <th>children</th>\n",
       "      <th>charges</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>1338.000000</td>\n",
       "      <td>1338.000000</td>\n",
       "      <td>1338.000000</td>\n",
       "      <td>1338.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>39.207025</td>\n",
       "      <td>30.663397</td>\n",
       "      <td>1.094918</td>\n",
       "      <td>13270.422265</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>14.049960</td>\n",
       "      <td>6.098187</td>\n",
       "      <td>1.205493</td>\n",
       "      <td>12110.011237</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>18.000000</td>\n",
       "      <td>15.960000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1121.873900</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>27.000000</td>\n",
       "      <td>26.296250</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>4740.287150</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>39.000000</td>\n",
       "      <td>30.400000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>9382.033000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>51.000000</td>\n",
       "      <td>34.693750</td>\n",
       "      <td>2.000000</td>\n",
       "      <td>16639.912515</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>64.000000</td>\n",
       "      <td>53.130000</td>\n",
       "      <td>5.000000</td>\n",
       "      <td>63770.428010</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               age          bmi     children       charges\n",
       "count  1338.000000  1338.000000  1338.000000   1338.000000\n",
       "mean     39.207025    30.663397     1.094918  13270.422265\n",
       "std      14.049960     6.098187     1.205493  12110.011237\n",
       "min      18.000000    15.960000     0.000000   1121.873900\n",
       "25%      27.000000    26.296250     0.000000   4740.287150\n",
       "50%      39.000000    30.400000     1.000000   9382.033000\n",
       "75%      51.000000    34.693750     2.000000  16639.912515\n",
       "max      64.000000    53.130000     5.000000  63770.428010"
      ]
     },
     "execution_count": 9,
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
   "execution_count": 13,
   "id": "6aac56ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      age     sex     bmi  children smoker     region      charges\n",
      "1248   18  female  39.820         0     no  southeast   1633.96180\n",
      "482    18  female  31.350         0     no  southeast   1622.18850\n",
      "492    18  female  25.080         0     no  northeast   2196.47320\n",
      "525    18  female  33.880         0     no  southeast  11482.63485\n",
      "529    18    male  25.460         0     no  northeast   1708.00140\n",
      "...   ...     ...     ...       ...    ...        ...          ...\n",
      "398    64    male  25.600         2     no  southwest  14988.43200\n",
      "335    64    male  34.500         0     no  southwest  13822.80300\n",
      "378    64  female  30.115         3     no  northwest  16455.70785\n",
      "1265   64    male  23.760         0    yes  southeast  26926.51440\n",
      "635    64    male  38.190         0     no  northeast  14410.93210\n",
      "\n",
      "[1338 rows x 7 columns]\n"
     ]
    }
   ],
   "source": [
    "# sort the data by age\n",
    "df_sorted = data.sort_values(by='age')\n",
    "\n",
    "# display the sorted data\n",
    "print(df_sorted)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "335ac2b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "age           47\n",
       "sex            2\n",
       "bmi          548\n",
       "children       6\n",
       "smoker         2\n",
       "region         4\n",
       "charges     1337\n",
       "dtype: int64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.nunique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "dde56d2f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "male      676\n",
      "female    662\n",
      "Name: sex, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "sex_counts = df['sex'].value_counts()\n",
    "print(sex_counts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "65bb3173",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sex     has_children\n",
      "female  no              289\n",
      "        yes             373\n",
      "male    no              285\n",
      "        yes             391\n",
      "Name: children, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# create a new column indicating whether the person has children or not\n",
    "df['has_children'] = df['children'].apply(lambda x: 'yes' if x > 0 else 'no')\n",
    "\n",
    "# group the data by gender and has_children\n",
    "grouped = df.groupby(['sex', 'has_children'])\n",
    "\n",
    "# count the number of people in each group\n",
    "counts = grouped['children'].count()\n",
    "\n",
    "# display the counts\n",
    "print(counts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "0f771dc6",
   "metadata": {},
   "outputs": [
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
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# determine the number of males and females\n",
    "sex_counts = df['sex'].value_counts()\n",
    "\n",
    "# create a bar plot\n",
    "sex_counts.plot(kind='bar', color=['red', 'blue'])\n",
    "\n",
    "# add a title and labels for the x and y axes\n",
    "plt.title('Number of Male and Female')\n",
    "plt.xlabel('Sex')\n",
    "plt.ylabel('Count')\n",
    "\n",
    "# display the plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "b833e05d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "sex     smoker\n",
      "female  no        547\n",
      "        yes       115\n",
      "male    no        517\n",
      "        yes       159\n",
      "Name: smoker, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# group the data by gender and smoker status\n",
    "grouped = df.groupby(['sex', 'smoker'])\n",
    "\n",
    "# count the number of people in each group\n",
    "counts = grouped['smoker'].count()\n",
    "\n",
    "# display the counts\n",
    "print(counts)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "95653331",
   "metadata": {},
   "outputs": [
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
    "# group the data by smoker and sex columns\n",
    "grouped = df.groupby(['smoker', 'sex']).size().reset_index(name='counts')\n",
    "\n",
    "# create separate dataframes for male and female smokers and non-smokers\n",
    "male_smokers = grouped[(grouped['smoker'] == 'yes') & (grouped['sex'] == 'male')]\n",
    "male_non_smokers = grouped[(grouped['smoker'] == 'no') & (grouped['sex'] == 'male')]\n",
    "female_smokers = grouped[(grouped['smoker'] == 'yes') & (grouped['sex'] == 'female')]\n",
    "female_non_smokers = grouped[(grouped['smoker'] == 'no') & (grouped['sex'] == 'female')]\n",
    "\n",
    "# plot the number of male and female smokers and non-smokers\n",
    "plt.bar(['Male Smoker', 'Male Non-Smoker', 'Female Smoker', 'Female Non-Smoker'], \n",
    "        [male_smokers['counts'].values[0], male_non_smokers['counts'].values[0], \n",
    "         female_smokers['counts'].values[0], female_non_smokers['counts'].values[0]], \n",
    "        color=['green', 'red', 'green', 'red'])\n",
    "\n",
    "# add a title and labels for the x and y axes\n",
    "plt.title('Number of Smokers and Non-Smokers by sex')\n",
    "plt.xlabel('Smoker Status by sex')\n",
    "plt.ylabel('Count')\n",
    "\n",
    "# display the plot\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "f7807a3a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "      sex     region  counts\n",
      "0  female  northeast     161\n",
      "1  female  northwest     164\n",
      "2  female  southeast     175\n",
      "3  female  southwest     162\n",
      "4    male  northeast     163\n",
      "5    male  northwest     161\n",
      "6    male  southeast     189\n",
      "7    male  southwest     163\n"
     ]
    }
   ],
   "source": [
    "gender_region_counts = df.groupby(['sex', 'region']).size().reset_index(name='counts')\n",
    "\n",
    "print(gender_region_counts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5b915ec0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "gender_region_counts = df.groupby(['sex', 'region']).size().reset_index(name='counts')\n",
    "\n",
    "# Plot the pie chart for each region\n",
    "for region, region_data in gender_region_counts.groupby('region'):\n",
    "    fig, ax = plt.subplots()\n",
    "    ax.pie(region_data['counts'], labels=region_data['sex'], autopct='%1.1f%%')\n",
    "    ax.set_title(f'Gender distribution in region {region}')\n",
    "    plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "52118302",
   "metadata": {},
   "outputs": [],
   "source": [
    "#There are roughly equal numbers of men and women in each region.\n",
    "#The distribution of male and female persons in the data is balanced.\n",
    "#The data includes details about a person's age, sex, BMI, how many children they have, if they smoke, and where they live together with charges.\n",
    "#The number of smokers and non-smokers both male and female are about same age on average"
   ]
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
