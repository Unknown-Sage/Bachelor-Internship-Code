
simdatael = [triboson_electron_n,top_electron_n,diboson_electron_n,higgs_electron_n]
simweightel = [triboson_weight,top_weight,diboson_weight,higgs_weight]
simdatahighel = [triboson_electron_n_high,top_electron_n_high,diboson_electron_n_high,higgs_electron_n_high]
simweighthighel = [triboson_weight_high,top_weight_high,diboson_weight_high,higgs_weight_high]
simdatalowel = [triboson_electron_n_low,top_electron_n_low,diboson_electron_n_low,higgs_electron_n_low]
simweightlowel = [triboson_weight_low,top_weight_low,diboson_weight_low,higgs_weight_low]

simdatamu = [triboson_muon_n,top_muon_n,diboson_muon_n,higgs_muon_n]
simweightmu = [triboson_weight,top_weight,diboson_weight,higgs_weight]
simdatahighmu = [triboson_muon_n_high,top_muon_n_high,diboson_muon_n_high,higgs_muon_n_high]
simweighthighmu = [triboson_weight_high,top_weight_high,diboson_weight_high,higgs_weight_high]
simdatalowmu = [triboson_muon_n_low,top_muon_n_low,diboson_muon_n_low,higgs_muon_n_low]
simweightlowmu = [triboson_weight_low,top_weight_low,diboson_weight_low,higgs_weight_low]


fig, (ax1, ax2) = plt.subplots(1,2)
#fig.suptitle('Electron Multiplicity')
ax1.hist(data_electron_n, bins=electron_n_bin,histtype='step',stacked=False,label='data')
ax1.hist(simdatael, bins=electron_n_bin,histtype='bar',weights=simweightel,stacked=True,label=['triboson','top','diboson','higgs'])
ax1.set_xlim([0,5])
ax1.set_xlabel('#electrons')
ax1.set_ylim([0,160])
ax1.set_ylabel('#events')
ax1.legend()
ax1.set_title('# of Electrons')

ax2.hist(data_muon_n, bins=electron_n_bin,histtype='step',stacked=False,label='data')
ax2.hist(simdatamu, bins=electron_n_bin,histtype='bar',weights=simweightmu,stacked=True,label=['triboson','top','diboson','higgs'])
ax2.set_xlim([0,5])
ax2.set_xlabel('#muons')
ax2.set_ylim([0,160])
ax2.set_ylabel('#events')
ax2.legend()
ax2.set_title('# of Muons')

fig2, (ax3, ax4) = plt.subplots(1,2)
ax3.hist(data_electron_n_high, bins=electron_n_bin,histtype='step',stacked=False,label='data')
ax3.hist(simdatahighel, bins=electron_n_bin,histtype='bar',weights=simweighthighel,stacked=True,label=['triboson','top','diboson','higgs'])
ax3.set_xlim([0,5])
ax3.set_xlabel('#electrons')
ax3.set_ylim([0,50])
ax3.set_ylabel('#events')
ax3.legend()
ax3.set_title('# of Electrons at MET > 50')

ax4.hist(data_muon_n_high, bins=electron_n_bin,histtype='step',stacked=False,label='data')
ax4.hist(simdatahighmu, bins=electron_n_bin,histtype='bar',weights=simweighthighmu,stacked=True,label=['triboson','top','diboson','higgs'])
ax4.set_xlim([0,5])
ax4.set_xlabel('#muons')
ax4.set_ylim([0,50])
ax4.set_ylabel('#events')
ax4.legend()
ax4.set_title('# of Muons at MET < 50')

fig3, (ax5, ax6) = plt.subplots(1,2)
ax5.hist(data_electron_n_low, bins=electron_n_bin,histtype='step',stacked=False,label='data')
ax5.hist(simdatalowel, bins=electron_n_bin,histtype='bar',weights=simweightlowel,stacked=True,label=['triboson','top','diboson','higgs'])
ax5.set_xlim([0,5])
ax5.set_xlabel('#electrons')
ax5.set_ylim([0,120])
ax5.set_ylabel('#events')
ax5.legend()
ax5.set_title('# of Electrons at MET > 50')

ax6.hist(data_muon_n_low, bins=electron_n_bin,histtype='step',stacked=False,label='data')
ax6.hist(simdatalowmu, bins=electron_n_bin,histtype='bar',weights=simweightlowmu,stacked=True,label=['triboson','top','diboson','higgs'])
ax6.set_xlim([0,5])
ax6.set_xlabel('#muons')
ax6.set_ylim([0,120])
ax6.set_ylabel('#events')
ax6.legend()
ax6.set_title('# of Muons at MET < 50')

plt.show()
