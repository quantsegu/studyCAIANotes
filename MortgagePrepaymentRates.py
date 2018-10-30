SingleMonthlyMortality = 0.0034
ConstantPrepaymentRate = 1 - (1 - SingleMonthlyMortality) ** 12
print(ConstantPrepaymentRate)
#PSAModel suggests a different approach this can be a multiple as well 
multipleOfPSAModel = 2.5
PSAInitial = 0.002 * multipleOfPSAModel
MonthsTill30 = 30 #can be any number below 60
PSATill_30_Months = PSAInitial * MonthsTill30
PSACPRRateAfter30Months = 0.06
print(PSATill_30_Months)
