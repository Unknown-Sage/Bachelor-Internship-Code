
simdataplus = [triboson_inv_mass_charge2,top_inv_mass_charge2,fake_inv_mass_charge2,diboson_inv_mass_charge2]
simweightplus = [triboson_weight_charge2,top_weight_charge2,fake_weight_charge2,diboson_weight_charge2]

simdatamin = [triboson_inv_mass_charge2min,top_inv_mass_charge2min,fake_inv_mass_charge2min,diboson_inv_mass_charge2min]
simweightmin = [triboson_weight_charge2min,top_weight_charge2min,fake_weight_charge2min,diboson_weight_charge2min]

fig, (ax1, ax2) = plt.subplots(1,2)

ax1.hist(data_inv_mass_charge2, bins=inv_mass_bin,histtype='step',stacked=False,label='data')
ax1.hist(simdataplus, bins=inv_mass_bin,histtype='bar',weights=simweightplus,stacked=True,label=['triboson','top','fake','diboson'])
ax1.set_xlim([100,800])
ax1.set_xlabel('invariant mass (GeV)')
ax1.set_ylim([0,4])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('Invariant Mass for total charge = 2')

ax2.hist(data_inv_mass_charge2min, bins=inv_mass_bin,histtype='step',stacked=False,label='data')
ax2.hist(simdatamin, bins=inv_mass_bin,histtype='bar',weights=simweightmin,stacked=True,label=['triboson','top','fake','diboson'])
ax2.set_xlim([100,800])
ax2.set_xlabel('invariant mass (GeV)')
ax2.set_ylim([0,4])
ax2.set_ylabel('#events')
ax2.legend()
ax2.set_title('Invariant Mass for total charge = -2')

plt.show()
