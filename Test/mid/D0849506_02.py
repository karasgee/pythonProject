import pandas as pd
import openpyxl
if __name__ == '__main__':
    momo_data_df = pd.read_excel("momo_product.xlsx")
    momo_data_dafr = pd.DataFrame(momo_data_df)

    for i in range(len(momo_data_df)):

            if momo_data_dafr['price'][i]<30000:

                    momo_data_dafr_2 = momo_data_dafr.drop(index= [i])

    print(momo_data_dafr_2)
    momo_data_dafr_2.to_excel("momo_product_result.xlsx")