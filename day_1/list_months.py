list_month=['jan','feb','mar','apr','may','jun','july','aug','sep','oct','nov','dec']
month=raw_input("enter number :")
month=int(month)
end=month*3
start=end-3
print list_month[start:end]