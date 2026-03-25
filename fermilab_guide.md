# Fermilab GPVM Guide

## 1. Before connecting (every time)

```bash
kinit -fr 7d junsulee@FNAL.GOV
ssh -XY junsulee@uboonegpvm01.fnal.gov
```

---

## 2. After connecting to the server (every time)

```bash
/cvmfs/uboone.opensciencegrid.org/bin/shell_apptainer.sh   # Enter SL7 container
source /exp/uboone/app/users/junsulee/setup.sh             # Set up environment
cd /exp/uboone/app/users/junsulee                          # Go to work directory
```

Contents of setup.sh:
```bash
source /cvmfs/uboone.opensciencegrid.org/products/setup_uboone.sh
setup uboonecode v08_00_00_61 -q e17:prof
```

---

## 3. Key paths

### My work directory
```
/exp/uboone/app/users/junsulee/
├── setup.sh
└── DarkTridentGen/
    ├── BdNMC/
    │   ├── bin/BDNMC          # Executable
    │   └── my_darktridentgen_test.root
    ├── xsec/
    ├── evgen.exe
    ├── pi0s.dat
    ├── etas.dat
    ├── rhc_pi0s.dat
    ├── rhc_etas.dat
    └── test_param.dat         # Parameter file
```

### Luis' reference directory
```
/exp/uboone/app/users/lmoralep/test_2025/
├── dark_trident_generator_4_grid_V2.tar.gz   # Original tarball
├── DarkTridentGen/                            # Unpacked generator
├── dark_trident_overlays/
└── generator/
```

### Home directory (do not work here - very limited storage)
```
/nashome/j/junsulee/
```

---

## 4. Running the generator

```bash
cd /exp/uboone/app/users/junsulee/DarkTridentGen
./BdNMC/bin/BDNMC test_param.dat
```

Output files:
- `BdNMC/my_darktridentgen_test.root` → Generated event data
- `BdNMC/my_summary_test.txt` → Run summary

---

## 5. Using ROOT

```bash
root BdNMC/my_darktridentgen_test.root   # Open ROOT file
```

Inside ROOT:
```
.ls                              # View file structure
event_tree->GetEntries()         # Check number of events
event_tree->Print()              # List all variables
event_tree->Draw("variable")     # Plot histogram
.q                               # Exit ROOT
```

---

## 6. Kerberos ticket management

- Ticket validity: 24 hours
- Renew (within 7 days): `kinit -R`
- Get new ticket: `kinit -fr 7d junsulee@FNAL.GOV`
- Check ticket: `klist`
