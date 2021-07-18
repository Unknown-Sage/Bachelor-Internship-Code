
simdata = [triboson_total_charge,top_total_charge,fake_total_charge,diboson_total_charge]
simweight = [triboson_weight,top_weight,fake_weight,diboson_weight]

combidata = np.concatenate((triboson_total_charge,top_total_charge,fake_total_charge,diboson_total_charge))
combiweight = np.concatenate((triboson_weight,top_weight,fake_weight,diboson_weight))

temp1 = plt.hist(combidata, bins=charge_bin,histtype='bar',weights=combiweight,stacked=True,label=['triboson','top','fake','diboson'])
temp2 = plt.hist(higgs_total_charge, bins=charge_bin,histtype='step',weights=higgs_weight,stacked=False,label='doubly charged higgs')

charge_scale = [-3,-2,-1,0,1,2,3]


fig, (ax1,ax2) = plt.subplots(1,2)
#fig.suptitle('Total charge distribution')

ax1.hist(higgs_total_charge, bins=charge_bin,histtype='step',weights=higgs_weight,stacked=True,label='higgs')
ax1.hist(simdata, bins=charge_bin,histtype='bar',weights=simweight,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_yscale('log')
ax1.set_xlim([-3,3])
ax1.set_xlabel('total elementary charge')
ax1.set_ylim([0.4,1000])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Total Charge Higgs Comparison')

s = temp2[0]
b = temp1[0]

comparisonvalue = s/np.sqrt(b)
comparisonvalue2 = np.sqrt(2*((temp2[0]+temp1[0])*np.log(1+temp2[0]/temp1[0])-temp2[0]))


ax2.plot(charge_scale,comparisonvalue,label='"simple" significance')
ax2.plot(charge_scale,comparisonvalue2,label='"complex" significance')
ax2.set_xlim([-3,3])
ax2.set_xlabel('significance')
ax2.set_ylim([0,5])
ax2.set_ylabel('#events')
ax2.legend()
ax2.set_title('Total Charge Higgs significance')

plt.show()
