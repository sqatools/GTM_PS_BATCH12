# Q2.  Calculate the electricity bill as per the unit consumed.
# get number of unit from user as input.
# if unit < 30 :  per unit charge is 5
# elif unit > 30 and unit < 200 :  per unit charge is 8
# elif unit > 90 :  per unit charge is 10
# else condition

#num_unit = int(input("Enter the number of units consumed :"))
#if num_unit < 30:
  #print("total bill as per 5/unit rate :", num_unit*5)
#elif num_unit >= 30 and num_unit <= 90:
  #  print("total bill as per 8/unit rate :", num_unit*8)
#elif num_unit >= 90:
  #print("total bill as per 10/unit rate :", num_unit * 10)

 # print("_" * 50)
##########################################################################################
  #keb_unit = int(input("Enter the number of units consumed :"))
  #if keb_unit < 30:
   #   print("total bill as per 5/unit rate :", keb_unit * 5)
  #elif keb_unit >= 30 and num_unit <= 90:
    #  print("total bill as per 8/unit rate :", keb_unit * 8)
  #elif keb_unit >= 90:
  #    print("total bill as per 10/unit rate :", keb_unit * 10)
#########################################################################

Free_unit = int(input("Enter free quota units:"))
if Free_unit <= 70:
    print("Free quota used govt of karnataka will pay so no bill enjoy :")
elif Free_unit >=71 :
    print ("Free quota Exceeds  Paid quota 8/Unit rate :",Free_unit*8)
