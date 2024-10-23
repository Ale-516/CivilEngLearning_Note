# Axially Loaded Members
This part will list a lot of equations to show the mathmatical work
## The consititutive law of the material
### concrete
when $\varepsilon_c < \varepsilon_0$  
$\sigma_c = 1000 \sigma_c (1-250 \varepsilon_c) f_c$  
when $\varepsilon_c > \varepsilon_0$  
$\sigma_c = f_c$
### reinforcement
when $\varepsilon_s < \varepsilon_y$  
$\sigma_s = E_s \varepsilon_s$  
when $\varepsilon_s > \varepsilon_0$  
$\sigma_s = f_y$
## Axial tension
**Before cracking:**
$$
\varepsilon = \varepsilon_s = \varepsilon_c \\
N_t = \varepsilon E_s A_s + \varepsilon E_c A = \varepsilon E_c (\alpha_E A_s + A) \\
= \varepsilon E_c A (\alpha_E \rho + 1)
$$
**Cracking load:**
$$
\varepsilon = \varepsilon_{t0} \\
N_{tcr} = \varepsilon_{t0} E_c A (\alpha_E \rho + 1)
$$
**After carcking but before reinforcement yield (the concrete'll quit working):**
$$
N_t = E_s \varepsilon A_s
$$
**Ultimate tension capacity**
$$
N_{tu} = E_s \varepsilon_y A_s = f_y A_s
$$

## Axial compression
### Situation 01: short column
1.  Before cracking:
    $$
    N_{c} = \sigma_{c} A + \sigma_{s}' A_s' \\
    \downarrow E_c'=vE_c \\
    N_t=vE_c \varepsilon_c A + E_s \varepsilon_s A_s' \\
    \downarrow \varepsilon_s = \varepsilon_c = \varepsilon \\
    N_t= v E_c \varepsilon A ( 1 + \frac{\alpha_E}{v} \rho'  )
    $$
2.  When cracking ($\varepsilon$ reach the yield point) 
    $$
    N_t|_{\varepsilon = \varepsilon_{t0}} = vE_c \varepsilon_{t0} A (1+\frac{\alpha_E}{v} \rho') \\ 
    $$
3.  After cracking ($\sigma_{ct} = 0$)
    $$
    N_{t}=\sigma_{st} A_s =E_s A_s \varepsilon
    $$
4.  Ultimate load
    $$
    N_t = f_{ys} A_s
    $$
5. If the concrete cracking and the steel yield at the same time
   $$

   $$
### Situation 02: long column
### Situation 03: Creep Influence
1. **Right after applying $N_c$**
    $$
    E_c'\varepsilon A + E_s \varepsilon A_s = N_c \\
    \rightarrow \varepsilon = \frac{N_c}{E_c' A + E_s A_s } \\
    \sigma_s = \varepsilon E_s = \frac{ N_c E_s }{ E_c' A + E_s A_s } = \frac{ N_c }{ \frac{ v }{ \rho' } A + A_s } = \frac{N_c}{ ( \frac{v}{\rho' \alpha_E}+1) A_s } \\
    \sigma_c = \varepsilon E_c = \frac{E_c N_c}{E_c'A + E_sA_s} = \frac{ N_c }{ vA + \frac{1}{\rho'}A_s } = \frac{N_c}{  }  
    $$
 
2. **Undergoing creep deformation**
3. **Remove $N_c$**