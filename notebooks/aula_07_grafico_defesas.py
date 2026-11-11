"""Recria a figura do relatório a partir das coortes, sem executar modelos."""
from pathlib import Path
import csv
ROOT=Path(__file__).resolve().parents[1]
with (ROOT/'resultados/aula-07/analise-final/coortes_baseline.csv').open(encoding='utf-8-sig',newline='') as f:
    cohorts=list(csv.DictReader(f))
for x in cohorts:
    for key in ['permanecem_sucesso','novos_sucessos','permanecem_falha']: x[key]=int(x[key])
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'axes.spines.top':False,'axes.spines.right':False,'pdf.fonttype':42})
fig,axes=plt.subplots(1,2,figsize=(7.4,3.25),layout='constrained')
x=np.arange(3);width=.32;colors=['#0072B2','#D55E00']
for ax,field,den,title in [(axes[0],'permanecem_sucesso',33,'(a) Sucessos no baseline (n = 33)'),(axes[1],'permanecem_falha',12,'(b) Falhas no baseline (n = 12)')]:
 for j,lang in enumerate(['EN','PT']):
  vals=[next(z[field] for z in cohorts if z['condicao']==d+'_'+lang) for d in ['SR','IA','SRIA']]
  bars=ax.bar(x+(j-.5)*width,vals,width,label=lang,color=colors[j],hatch='///' if j else None,edgecolor='white',linewidth=.5,zorder=3)
  for bar,v in zip(bars,vals):
   inside=den==12 and v>0
   ax.text(bar.get_x()+bar.get_width()/2,v-.45 if inside else v+.45,str(v),ha='center',va='top' if inside else 'bottom',color='white' if inside else 'black',fontsize=10,fontweight='bold')
 ax.set_xticks(x,['SR','IA','SR + IA']);ax.set_ylim(0,den+3);ax.set_title(title,fontsize=10.5,fontweight='bold',pad=10);ax.set_ylabel('Sucessos mantidos após a defesa' if den==33 else 'Falhas mantidas após a defesa');ax.set_axisbelow(True);ax.yaxis.grid(True,color='#e5e7eb',linewidth=.7)
 ax.set_yticks([0,5,10,15,20,25,30,33] if den==33 else [0,2,4,6,8,10,12])
 baseline=next(z[field] for z in cohorts if z['condicao']=='B')
 ax.axhline(baseline,color='#111827',linewidth=1.8 if den==12 else 1.35,linestyle=(0,(5,3)),zorder=6)
 if den==33:
  ax.set_ylim(0,39)
  ax.text(.02,baseline+.5,'Baseline: 33',transform=ax.get_yaxis_transform(),ha='left',va='bottom',fontsize=9,color='#374151',bbox=dict(facecolor='white',edgecolor='none',pad=.5))
 else:
  ax.set_ylim(0,16.5)
  ax.text(.02,baseline+.5,'Baseline: 12',transform=ax.get_yaxis_transform(),ha='left',va='bottom',fontsize=9,color='#374151',bbox=dict(facecolor='white',edgecolor='none',pad=.5))
 ax.legend(frameon=False,ncol=2,loc='upper right')
figdir=ROOT/'images/aula-07';figdir.mkdir(parents=True,exist_ok=True)
fig.savefig(figdir/'efeito-defesas-baseline.png',dpi=320,facecolor='white')
plt.close(fig)
