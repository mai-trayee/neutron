# neutron

event.txt produced from output of (on sukap) 
> root -l /disk02/usr6/mandal/21b/sk4/nnfriend/taumc/h1/sk4.taumc.h1.000.root
root [0] 
Attaching file /disk02/usr6/mandal/21b/sk4/nnfriend/taumc/h1/sk4.taumc.h1.000.root as _file0...
root [1]  h1->Scan("nscndprt:iprntprt:iprtscnd:lmecscnd:iorgprt:tscnd:sqrt(pscnd[0]*pscnd[0]+pscnd[1]*pscnd[1]+pscnd[2]*pscnd[2]):sqrt(pprnt[0]*pprnt[0]+pprnt[1]*pprnt[1]+pprnt[2]*pprnt[2]):sqrt(pprntinit[0]*pprntinit[0]+pprntinit[1]*pprntinit[1]+pprntinit[2]*pprntinit[2])","nev==99")
 



<CONVVECT> ( Copy of VECT2 secondaries stack with additional information )

nscndprt      : Number                        of secondary particles
(not used) itrkscnd      : Parent track number (GEANT)   of the secondary particle
istakscnd     : Parent stack track number (GEANT) of the secondary particle
(not used) vtxscnd       : Vertex                        of the generated point
pscnd         : Momentum                      of the secondary particle
iprtscnd      : Particle code                 of the secondary particle
tscnd         : Generated time                of the secondary particle
iprntprt      : Parent particle code          of the secondary particle
lmecscnd      : Interaction code (GEANT) that produced the secondary particle,
                 from GEANT3 documentation:
                    5: Decay
                    6: Pair production
                    7: Compton Scatter
                    8: Photo-electric
                    9: Bremsstrahlung
                    12: Hadronic Interaction
                    13: Hadronic Elastic Coherent Scattering
                    18: Neutron Capture
                    20: Hadronic Inelastic
                    21: Muon-Nuclear Interaction
                    23: Photonuclear
                    30: Below tracking threshold
(not used) iprnttrk      : Parent track number (VECT)  of the secondary particle
(not used) iorgprt       : Parent track PID code (VECT) of the secondary particle
(not used) iprntidx      : Array index (Fortran) of this secondary particle\'s parent
                   Negative: Index corresponding to VCWORK (NEUT) stack
                   Positive: Index corresponding to this stack
                   0: Unmatched (E.g. muon or hadron > 10 GeV/c)
(not used) nchilds       : Number of daughter particles (NGKINE in GEANT)
(not used) ichildidx     : Array index (Fortran) in this stack of this secondary particle's first child
                   0: No matched children
pprnt         : Momentum                      of the parent particle at interaction
pprntinit     : Initial momentum              of the parent particle at birth
(not used) vtxprnt       : Vertex                        of the parent particle at birth


lmecscnd has been added from
https://indico-sk.icrr.u-tokyo.ac.jp/event/2140/contributions/2870/attachments/3100/3616/fqworkshop_scndryinfo.pdf
