
# Run docking sim assuming receptor is rigid
vina --center_x 11 --center_y 90.5 --center_z 57.5 \
     --size_x 22 --size_y 24 --size_z 28 \
     --receptor input/receptor_rigid.pdbqt \
     --ligand input/ligand.pdbqt \
     --exhaustiveness 8 \
     --log results/rigid/vina.log

vina_split --input input/ligand_out.pdbqt \
	   --ligand results/rigid/ligand

rm input/ligand_out.pdbqt

# Run docking sim assuming receptor has flexible sidechains
vina --center_x 11 --center_y 90.5 --center_z 57.5 \
     --size_x 22 --size_y 24 --size_z 28 \
     --receptor input/receptor_rigid.pdbqt \
     --ligand input/ligand.pdbqt \
     --exhaustiveness 8 \
     --log results/flexible/vina.log

vina_split --input input/ligand_out.pdbqt \
	   --ligand results/flexible/ligand \
	   --flex results/flexible/sideChains.pdbqt

rm input/ligand_out.pdbqt
