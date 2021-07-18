
simdata = [triboson_inv_mass,top_inv_mass,fake_inv_mass,diboson_inv_mass]
simweight = [triboson_weight,top_weight,fake_weight,diboson_weight]
simdatahigh = [triboson_inv_mass_high,top_inv_mass_high,fake_inv_mass_high,diboson_inv_mass_high]
simweighthigh = [triboson_weight_high,top_weight_high,fake_weight_high,diboson_weight_high]
simdatalow = [triboson_inv_mass_low,top_inv_mass_low,fake_inv_mass_low,diboson_inv_mass_low]
simweightlow = [triboson_weight_low,top_weight_low,fake_weight_low,diboson_weight_low]


fig, (ax1, ax2, ax3 ) = plt.subplots(1,3)
#fig.suptitle('Invariant Mass')
ax1.hist(data_inv_mass, bins=inv_mass_bin,histtype='step',stacked=False,label='data')
ax1.hist(simdata, bins=inv_mass_bin,histtype='bar',weights=simweight,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_yscale('log')
ax1.set_xlim([100,800])
ax1.set_xlabel('invariant mass (GeV)')
ax1.set_ylim([0.4,2500])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Invariant Mass')

ax2.hist(data_inv_mass_low, bins=inv_mass_bin,histtype='step',stacked=False,label='data')
ax2.hist(simdatalow, bins=inv_mass_bin,histtype='bar',weights=simweightlow,stacked=True,label=['triboson','top','fake','diboson'])
ax2.set_yscale('log')
ax2.set_xlim([100,800])
ax2.set_xlabel('invariant mass (GeV)')
ax2.set_ylim([0.4,2500])
ax2.set_ylabel('#events')
ax2.legend()
ax2.set_title('Invariant Mass with Missing E_t < 50')

ax3.hist(data_inv_mass_high, bins=inv_mass_bin,histtype='step',stacked=False,label='data')
ax3.hist(simdatahigh, bins=inv_mass_bin,histtype='bar',weights=simweighthigh,stacked=True,label=['triboson','top','fake','diboson'])
ax3.set_yscale('log')
ax3.set_xlim([100,800])
ax3.set_xlabel('invariant mass (GeV)')
ax3.set_ylim([0.4,2500])
ax3.set_ylabel('#events')
ax3.legend()
ax3.set_title('Invariant Mass with Missing E_t > 50')

plt.show()
