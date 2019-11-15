/* I generated this file with GCC after discovering the "-fverbose-asm" flag.
   I found it so interesting that I decided to keep it. It is compiled from
   the physics program that I wrote. */

	.file	"main.c"
# GNU C11 (Ubuntu 7.4.0-1ubuntu1~18.04.1) version 7.4.0 (x86_64-linux-gnu)
#	compiled by GNU C version 7.4.0, GMP version 6.1.2, MPFR version 4.0.1, MPC version 1.1.0, isl version isl-0.19-GMP

# GGC heuristics: --param ggc-min-expand=100 --param ggc-min-heapsize=131072
# options passed:  -I /usr/include/SDL2 -imultiarch x86_64-linux-gnu
# -D _REENTRANT main.c -mtune=generic -march=x86-64 -fverbose-asm
# -fstack-protector-strong -Wformat -Wformat-security
# options enabled:  -fPIC -fPIE -faggressive-loop-optimizations
# -fasynchronous-unwind-tables -fauto-inc-dec -fchkp-check-incomplete-type
# -fchkp-check-read -fchkp-check-write -fchkp-instrument-calls
# -fchkp-narrow-bounds -fchkp-optimize -fchkp-store-bounds
# -fchkp-use-static-bounds -fchkp-use-static-const-bounds
# -fchkp-use-wrappers -fcommon -fdelete-null-pointer-checks
# -fdwarf2-cfi-asm -fearly-inlining -feliminate-unused-debug-types
# -ffp-int-builtin-inexact -ffunction-cse -fgcse-lm -fgnu-runtime
# -fgnu-unique -fident -finline-atomics -fira-hoist-pressure
# -fira-share-save-slots -fira-share-spill-slots -fivopts
# -fkeep-static-consts -fleading-underscore -flifetime-dse
# -flto-odr-type-merging -fmath-errno -fmerge-debug-strings -fpeephole
# -fplt -fprefetch-loop-arrays -freg-struct-return
# -fsched-critical-path-heuristic -fsched-dep-count-heuristic
# -fsched-group-heuristic -fsched-interblock -fsched-last-insn-heuristic
# -fsched-rank-heuristic -fsched-spec -fsched-spec-insn-heuristic
# -fsched-stalled-insns-dep -fschedule-fusion -fsemantic-interposition
# -fshow-column -fshrink-wrap-separate -fsigned-zeros
# -fsplit-ivs-in-unroller -fssa-backprop -fstack-protector-strong
# -fstdarg-opt -fstrict-volatile-bitfields -fsync-libcalls -ftrapping-math
# -ftree-cselim -ftree-forwprop -ftree-loop-if-convert -ftree-loop-im
# -ftree-loop-ivcanon -ftree-loop-optimize -ftree-parallelize-loops=
# -ftree-phiprop -ftree-reassoc -ftree-scev-cprop -funit-at-a-time
# -funwind-tables -fverbose-asm -fzero-initialized-in-bss
# -m128bit-long-double -m64 -m80387 -malign-stringops
# -mavx256-split-unaligned-load -mavx256-split-unaligned-store
# -mfancy-math-387 -mfp-ret-in-387 -mfxsr -mglibc -mieee-fp
# -mlong-double-80 -mmmx -mno-sse4 -mpush-args -mred-zone -msse -msse2
# -mstv -mtls-direct-seg-refs -mvzeroupper

	.text
	.section	.rodata
	.align 8
.LC0:
	.string	"Physics Sim in pure C (press X to close)"
	.align 8
.LC1:
	.string	"Error! Something went horribly wrong!"
.LC2:
	.string	"Error: %s\n"
.LC7:
	.string	"Closing the program."
	.text
	.globl	main
	.type	main, @function
main:
.LFB3676:
	.cfi_startproc
	pushq	%rbp	#
	.cfi_def_cfa_offset 16
	.cfi_offset 6, -16
	movq	%rsp, %rbp	#,
	.cfi_def_cfa_register 6
	pushq	%rbx	#
	subq	$184, %rsp	#,
	.cfi_offset 3, -24
	movl	%edi, -164(%rbp)	# argc, argc
	movq	%rsi, -176(%rbp)	# argv, argv
# main.c:36: int main(int argc, char *argv[]) {
	movq	%fs:40, %rax	#, tmp306
	movq	%rax, -24(%rbp)	# tmp306, D.27368
	xorl	%eax, %eax	# tmp306
# main.c:37:     SDL_Init(SDL_INIT_VIDEO);
	movl	$32, %edi	#,
	call	SDL_Init@PLT	#
# main.c:40:     SDL_Window *main_window = SDL_CreateWindow(
	movl	$0, %r9d	#,
	movl	$400, %r8d	#,
	movl	$400, %ecx	#,
	movl	$805240832, %edx	#,
	movl	$805240832, %esi	#,
	leaq	.LC0(%rip), %rdi	#,
	call	SDL_CreateWindow@PLT	#
	movq	%rax, -120(%rbp)	# tmp226, main_window
# main.c:50:     SDL_Renderer *renderer = SDL_CreateRenderer(
	movq	-120(%rbp), %rax	# main_window, tmp227
	movl	$0, %edx	#,
	movl	$0, %esi	#,
	movq	%rax, %rdi	# tmp227,
	call	SDL_CreateRenderer@PLT	#
	movq	%rax, -112(%rbp)	# tmp228, renderer
# main.c:57:     if (main_window == NULL || renderer == NULL) {
	cmpq	$0, -120(%rbp)	#, main_window
	je	.L2	#,
# main.c:57:     if (main_window == NULL || renderer == NULL) {
	cmpq	$0, -112(%rbp)	#, renderer
	jne	.L3	#,
.L2:
# main.c:58:         printf("Error! Something went horribly wrong!\n");
	leaq	.LC1(%rip), %rdi	#,
	call	puts@PLT	#
# main.c:59:         printf("Error: %s\n", SDL_GetError());
	call	SDL_GetError@PLT	#
	movq	%rax, %rsi	# _1,
	leaq	.LC2(%rip), %rdi	#,
	movl	$0, %eax	#,
	call	printf@PLT	#
# main.c:60:         return 1;
	movl	$1, %eax	#, _153
	jmp	.L32	#
.L3:
# main.c:63:     int window_open = 1; // will be set to 0 when it's time to close the window
	movl	$1, -144(%rbp)	#, window_open
# main.c:69:     Particle *mouse_particle = create_particle(0, 0, 0, 0);
	pxor	%xmm3, %xmm3	#
	pxor	%xmm2, %xmm2	#
	pxor	%xmm1, %xmm1	#
	pxor	%xmm0, %xmm0	#
	call	create_particle@PLT	#
	movq	%rax, -104(%rbp)	# tmp229, mouse_particle
# main.c:72:     Particle **particles = malloc(PARTICLE_CT * sizeof(Particle *));
	movl	$2048, %edi	#,
	call	malloc@PLT	#
	movq	%rax, -96(%rbp)	# tmp230, particles
# main.c:74:     for (i = 0; i < PARTICLE_CT; i++) {
	movl	$0, -140(%rbp)	#, i
	jmp	.L5	#
.L6:
# main.c:79:             (WINDOW_DIM / 2) + 20 * cos(i),
	cvtsi2sd	-140(%rbp), %xmm0	# casts i from int to double
	call	cos@PLT	#
	movapd	%xmm0, %xmm1	#, _3
	movsd	.LC4(%rip), %xmm0	#, tmp231
	mulsd	%xmm1, %xmm0	# _3, _4
	movsd	.LC5(%rip), %xmm1	#, tmp232
	addsd	%xmm1, %xmm0	# tmp232, _5
# main.c:75:         particles[i] = create_particle(
	cvtsd2ss	%xmm0, %xmm4	# _5, _6
	movss	%xmm4, -184(%rbp)	# _6, %sfp
# main.c:78:             (WINDOW_DIM / 2) + 20 * sin(i),
	cvtsi2sd	-140(%rbp), %xmm0	# i, _7
	call	sin@PLT	#
	movapd	%xmm0, %xmm1	#, _8
	movsd	.LC4(%rip), %xmm0	#, tmp233
	mulsd	%xmm1, %xmm0	# _8, _9
	movsd	.LC5(%rip), %xmm1	#, tmp234
	addsd	%xmm1, %xmm0	# tmp234, _10
# main.c:75:         particles[i] = create_particle(
	cvtsd2ss	%xmm0, %xmm0	# _10, _11
	movl	-140(%rbp), %eax	# i, tmp235
	cltq
	leaq	0(,%rax,8), %rdx	#, _13
	movq	-96(%rbp), %rax	# particles, tmp236
	leaq	(%rdx,%rax), %rbx	#, _14
	pxor	%xmm3, %xmm3	#
	pxor	%xmm2, %xmm2	#
	movss	-184(%rbp), %xmm1	# %sfp,
	call	create_particle@PLT	#
	movq	%rax, (%rbx)	# _15, *_14
# main.c:74:     for (i = 0; i < PARTICLE_CT; i++) {
	addl	$1, -140(%rbp)	#, i
.L5:
# main.c:74:     for (i = 0; i < PARTICLE_CT; i++) {
	cmpl	$255, -140(%rbp)	#, i
	jle	.L6	#,
# main.c:87:     Particle **prev_frame_particles = malloc(PARTICLE_CT * sizeof(Particle *));
	movl	$2048, %edi	#,
	call	malloc@PLT	#
	movq	%rax, -88(%rbp)	# tmp237, prev_frame_particles
# main.c:88:     for (i = 0; i < PARTICLE_CT; i++) {
	movl	$0, -140(%rbp)	#, i
	jmp	.L7	#
.L8:
# main.c:89:         prev_frame_particles[i] = create_particle(0, 0, 0, 0);
	movl	-140(%rbp), %eax	# i, tmp238
	cltq
	leaq	0(,%rax,8), %rdx	#, _17
	movq	-88(%rbp), %rax	# prev_frame_particles, tmp239
	leaq	(%rdx,%rax), %rbx	#, _18
	pxor	%xmm3, %xmm3	#
	pxor	%xmm2, %xmm2	#
	pxor	%xmm1, %xmm1	#
	pxor	%xmm0, %xmm0	#
	call	create_particle@PLT	#
	movq	%rax, (%rbx)	# _19, *_18
# main.c:88:     for (i = 0; i < PARTICLE_CT; i++) {
	addl	$1, -140(%rbp)	#, i
.L7:
# main.c:88:     for (i = 0; i < PARTICLE_CT; i++) {
	cmpl	$255, -140(%rbp)	#, i
	jle	.L8	#,
# main.c:92:     while (window_open) {
	jmp	.L9	#
.L29:
# main.c:94:         prev_mouse_x = mouse_x;
	movl	-152(%rbp), %eax	# mouse_x, tmp240
	movl	%eax, -128(%rbp)	# tmp240, prev_mouse_x
# main.c:95:         prev_mouse_y = mouse_y;
	movl	-148(%rbp), %eax	# mouse_y, tmp241
	movl	%eax, -124(%rbp)	# tmp241, prev_mouse_y
# main.c:98:         SDL_GetMouseState(
	leaq	-148(%rbp), %rdx	#, tmp242
	leaq	-152(%rbp), %rax	#, tmp243
	movq	%rdx, %rsi	# tmp242,
	movq	%rax, %rdi	# tmp243,
	call	SDL_GetMouseState@PLT	#
# main.c:104:         mouse_particle->x_pos = (float) mouse_x;
	movl	-152(%rbp), %eax	# mouse_x, mouse_x.0_20
	cvtsi2ss	%eax, %xmm0	# mouse_x.0_20, _21
	movq	-104(%rbp), %rax	# mouse_particle, tmp244
	movss	%xmm0, (%rax)	# _21, mouse_particle_175->x_pos
# main.c:105:         mouse_particle->y_pos = (float) mouse_y;
	movl	-148(%rbp), %eax	# mouse_y, mouse_y.1_22
	cvtsi2ss	%eax, %xmm0	# mouse_y.1_22, _23
	movq	-104(%rbp), %rax	# mouse_particle, tmp245
	movss	%xmm0, 4(%rax)	# _23, mouse_particle_175->y_pos
# main.c:106:         mouse_particle->x_momentum = (float) mouse_x - prev_mouse_x;
	movl	-152(%rbp), %eax	# mouse_x, mouse_x.2_24
	cvtsi2ss	%eax, %xmm0	# mouse_x.2_24, _25
	cvtsi2ss	-128(%rbp), %xmm1	# prev_mouse_x, _26
	subss	%xmm1, %xmm0	# _26, _27
	movq	-104(%rbp), %rax	# mouse_particle, tmp246
	movss	%xmm0, 8(%rax)	# _27, mouse_particle_175->x_momentum
# main.c:107:         mouse_particle->y_momentum = (float) mouse_y - prev_mouse_y;
	movl	-148(%rbp), %eax	# mouse_y, mouse_y.3_28
	cvtsi2ss	%eax, %xmm0	# mouse_y.3_28, _29
	cvtsi2ss	-124(%rbp), %xmm1	# prev_mouse_y, _30
	subss	%xmm1, %xmm0	# _30, _31
	movq	-104(%rbp), %rax	# mouse_particle, tmp247
	movss	%xmm0, 12(%rax)	# _31, mouse_particle_175->y_momentum
# main.c:111:             (mouse_x > 0 && mouse_x < WINDOW_DIM)
	movl	-152(%rbp), %eax	# mouse_x, mouse_x.4_32
# main.c:110:         if (
	testl	%eax, %eax	# mouse_x.4_32
	jle	.L10	#,
# main.c:111:             (mouse_x > 0 && mouse_x < WINDOW_DIM)
	movl	-152(%rbp), %eax	# mouse_x, mouse_x.5_33
	cmpl	$399, %eax	#, mouse_x.5_33
	jg	.L10	#,
# main.c:113:             (mouse_y > 0 && mouse_y < WINDOW_DIM)
	movl	-148(%rbp), %eax	# mouse_y, mouse_y.6_34
# main.c:112:         &&
	testl	%eax, %eax	# mouse_y.6_34
	jle	.L10	#,
# main.c:113:             (mouse_y > 0 && mouse_y < WINDOW_DIM)
	movl	-148(%rbp), %eax	# mouse_y, mouse_y.7_35
	cmpl	$399, %eax	#, mouse_y.7_35
	jg	.L10	#,
# main.c:115:             SDL_ShowCursor(SDL_DISABLE);
	movl	$0, %edi	#,
	call	SDL_ShowCursor@PLT	#
	jmp	.L11	#
.L10:
# main.c:117:             SDL_ShowCursor(SDL_ENABLE);
	movl	$1, %edi	#,
	call	SDL_ShowCursor@PLT	#
.L11:
# main.c:121:         for (i = 0; i < PARTICLE_CT; i++) {
	movl	$0, -140(%rbp)	#, i
	jmp	.L12	#
.L13:
# main.c:122:             copy_particle(prev_frame_particles[i], *particles[i]);
	movl	-140(%rbp), %eax	# i, tmp248
	cltq
	leaq	0(,%rax,8), %rdx	#, _37
	movq	-96(%rbp), %rax	# particles, tmp249
	addq	%rdx, %rax	# _37, _38
	movq	(%rax), %rax	# *_38, _39
	movl	-140(%rbp), %edx	# i, tmp250
	movslq	%edx, %rdx	# tmp250, _40
	leaq	0(,%rdx,8), %rcx	#, _41
	movq	-88(%rbp), %rdx	# prev_frame_particles, tmp251
	addq	%rcx, %rdx	# _41, _42
	movq	(%rdx), %rdx	# *_42, _43
	movq	(%rax), %rcx	# *_39, tmp252
	movq	8(%rax), %rax	# *_39, tmp253
	movq	%rcx, -184(%rbp)	# tmp252, %sfp
	movq	-184(%rbp), %xmm0	# %sfp,
	movq	%rax, -184(%rbp)	# tmp253, %sfp
	movq	-184(%rbp), %xmm1	# %sfp,
	movq	%rdx, %rdi	# _43,
	call	copy_particle@PLT	#
# main.c:121:         for (i = 0; i < PARTICLE_CT; i++) {
	addl	$1, -140(%rbp)	#, i
.L12:
# main.c:121:         for (i = 0; i < PARTICLE_CT; i++) {
	cmpl	$255, -140(%rbp)	#, i
	jle	.L13	#,
# main.c:125:         int j, bounce_direction = 0;
	movl	$0, -132(%rbp)	#, bounce_direction
# main.c:126:         for (i = 0; i < PARTICLE_CT; i++) {
	movl	$0, -140(%rbp)	#, i
	jmp	.L14	#
.L21:
# main.c:127:             if (bounce_direction > 3) bounce_direction = 0;
	cmpl	$3, -132(%rbp)	#, bounce_direction
	jle	.L15	#,
# main.c:127:             if (bounce_direction > 3) bounce_direction = 0;
	movl	$0, -132(%rbp)	#, bounce_direction
.L15:
# main.c:128:             for (j = 0; j < PARTICLE_CT; j++) {
	movl	$0, -136(%rbp)	#, j
	jmp	.L16	#
.L19:
# main.c:129:                 if (bounce_direction > 3) bounce_direction = 0;
	cmpl	$3, -132(%rbp)	#, bounce_direction
	jle	.L17	#,
# main.c:129:                 if (bounce_direction > 3) bounce_direction = 0;
	movl	$0, -132(%rbp)	#, bounce_direction
.L17:
# main.c:130:                 if (i != j) {
	movl	-140(%rbp), %eax	# i, tmp254
	cmpl	-136(%rbp), %eax	# j, tmp254
	je	.L18	#,
# main.c:138:                             prev_frame_particles[j]->y_pos,
	movl	-136(%rbp), %eax	# j, tmp255
	cltq
	leaq	0(,%rax,8), %rdx	#, _45
	movq	-88(%rbp), %rax	# prev_frame_particles, tmp256
	addq	%rdx, %rax	# _45, _46
	movq	(%rax), %rax	# *_46, _47
	movss	4(%rax), %xmm0	# _47->y_pos, _48
# main.c:134:                         is_distance(
	cvttss2si	%xmm0, %ecx	# _48, _49
# main.c:137:                             prev_frame_particles[j]->x_pos,
	movl	-136(%rbp), %eax	# j, tmp257
	cltq
	leaq	0(,%rax,8), %rdx	#, _51
	movq	-88(%rbp), %rax	# prev_frame_particles, tmp258
	addq	%rdx, %rax	# _51, _52
	movq	(%rax), %rax	# *_52, _53
	movss	(%rax), %xmm0	# _53->x_pos, _54
# main.c:134:                         is_distance(
	cvttss2si	%xmm0, %edx	# _54, _55
# main.c:136:                             particles[i]->y_pos,
	movl	-140(%rbp), %eax	# i, tmp259
	cltq
	leaq	0(,%rax,8), %rsi	#, _57
	movq	-96(%rbp), %rax	# particles, tmp260
	addq	%rsi, %rax	# _57, _58
	movq	(%rax), %rax	# *_58, _59
	movss	4(%rax), %xmm0	# _59->y_pos, _60
# main.c:134:                         is_distance(
	cvttss2si	%xmm0, %esi	# _60, _61
# main.c:135:                             particles[i]->x_pos,
	movl	-140(%rbp), %eax	# i, tmp261
	cltq
	leaq	0(,%rax,8), %rdi	#, _63
	movq	-96(%rbp), %rax	# particles, tmp262
	addq	%rdi, %rax	# _63, _64
	movq	(%rax), %rax	# *_64, _65
	movss	(%rax), %xmm0	# _65->x_pos, _66
# main.c:134:                         is_distance(
	cvttss2si	%xmm0, %eax	# _66, _67
	movss	.LC6(%rip), %xmm0	#,
	movl	%eax, %edi	# _67,
	call	is_distance@PLT	#
# main.c:133:                     if (
	testl	%eax, %eax	# _68
	je	.L18	#,
# main.c:144:                             *prev_frame_particles[j],
	movl	-136(%rbp), %eax	# j, tmp263
	cltq
	leaq	0(,%rax,8), %rdx	#, _70
	movq	-88(%rbp), %rax	# prev_frame_particles, tmp264
	addq	%rdx, %rax	# _70, _71
	movq	(%rax), %rax	# *_71, _72
# main.c:143:                             particles[i],
	movl	-140(%rbp), %edx	# i, tmp265
	movslq	%edx, %rdx	# tmp265, _73
	leaq	0(,%rdx,8), %rcx	#, _74
	movq	-96(%rbp), %rdx	# particles, tmp266
	addq	%rcx, %rdx	# _74, _75
# main.c:142:                         collide(
	movq	(%rdx), %rdx	# *_75, _76
	movl	-132(%rbp), %ecx	# bounce_direction, tmp267
	movq	(%rax), %rdi	# *_72, tmp268
	movq	8(%rax), %rax	# *_72, tmp269
	movl	%ecx, %esi	# tmp267,
	movq	%rdi, -184(%rbp)	# tmp268, %sfp
	movq	-184(%rbp), %xmm0	# %sfp,
	movq	%rax, -184(%rbp)	# tmp269, %sfp
	movq	-184(%rbp), %xmm1	# %sfp,
	movq	%rdx, %rdi	# _76,
	call	collide@PLT	#
# main.c:147:                         bounce_direction++;
	addl	$1, -132(%rbp)	#, bounce_direction
.L18:
# main.c:128:             for (j = 0; j < PARTICLE_CT; j++) {
	addl	$1, -136(%rbp)	#, j
.L16:
# main.c:128:             for (j = 0; j < PARTICLE_CT; j++) {
	cmpl	$255, -136(%rbp)	#, j
	jle	.L19	#,
# main.c:160:                     (float) mouse_y,
	movl	-148(%rbp), %eax	# mouse_y, mouse_y.8_77
	cvtsi2ss	%eax, %xmm0	# mouse_y.8_77, _78
# main.c:156:                 is_distance(
	cvttss2si	%xmm0, %ecx	# _78, _79
# main.c:159:                     (float) mouse_x,
	movl	-152(%rbp), %eax	# mouse_x, mouse_x.9_80
	cvtsi2ss	%eax, %xmm0	# mouse_x.9_80, _81
# main.c:156:                 is_distance(
	cvttss2si	%xmm0, %edx	# _81, _82
# main.c:158:                     particles[i]->y_pos,
	movl	-140(%rbp), %eax	# i, tmp270
	cltq
	leaq	0(,%rax,8), %rsi	#, _84
	movq	-96(%rbp), %rax	# particles, tmp271
	addq	%rsi, %rax	# _84, _85
	movq	(%rax), %rax	# *_85, _86
	movss	4(%rax), %xmm0	# _86->y_pos, _87
# main.c:156:                 is_distance(
	cvttss2si	%xmm0, %esi	# _87, _88
# main.c:157:                     particles[i]->x_pos,
	movl	-140(%rbp), %eax	# i, tmp272
	cltq
	leaq	0(,%rax,8), %rdi	#, _90
	movq	-96(%rbp), %rax	# particles, tmp273
	addq	%rdi, %rax	# _90, _91
	movq	(%rax), %rax	# *_91, _92
	movss	(%rax), %xmm0	# _92->x_pos, _93
# main.c:156:                 is_distance(
	cvttss2si	%xmm0, %eax	# _93, _94
	movss	.LC6(%rip), %xmm0	#,
	movl	%eax, %edi	# _94,
	call	is_distance@PLT	#
# main.c:155:             if (
	testl	%eax, %eax	# _95
	je	.L20	#,
# main.c:165:                     particles[i],
	movl	-140(%rbp), %eax	# i, tmp274
	cltq
	leaq	0(,%rax,8), %rdx	#, _97
	movq	-96(%rbp), %rax	# particles, tmp275
	addq	%rdx, %rax	# _97, _98
# main.c:164:                 collide(
	movq	(%rax), %rdx	# *_98, _99
	movl	-132(%rbp), %ecx	# bounce_direction, tmp276
	movq	-104(%rbp), %rax	# mouse_particle, tmp277
	movq	(%rax), %rdi	# *mouse_particle_175, tmp278
	movq	8(%rax), %rax	# *mouse_particle_175, tmp279
	movl	%ecx, %esi	# tmp276,
	movq	%rdi, -184(%rbp)	# tmp278, %sfp
	movq	-184(%rbp), %xmm0	# %sfp,
	movq	%rax, -184(%rbp)	# tmp279, %sfp
	movq	-184(%rbp), %xmm1	# %sfp,
	movq	%rdx, %rdi	# _99,
	call	collide@PLT	#
# main.c:169:                 bounce_direction++;
	addl	$1, -132(%rbp)	#, bounce_direction
.L20:
# main.c:173:             update_particle(particles[i], mouse_x, mouse_y);
	movl	-148(%rbp), %edx	# mouse_y, mouse_y.10_100
	movl	-152(%rbp), %ecx	# mouse_x, mouse_x.11_101
	movl	-140(%rbp), %eax	# i, tmp280
	cltq
	leaq	0(,%rax,8), %rsi	#, _103
	movq	-96(%rbp), %rax	# particles, tmp281
	addq	%rsi, %rax	# _103, _104
	movq	(%rax), %rax	# *_104, _105
	movl	%ecx, %esi	# mouse_x.11_101,
	movq	%rax, %rdi	# _105,
	call	update_particle@PLT	#
# main.c:126:         for (i = 0; i < PARTICLE_CT; i++) {
	addl	$1, -140(%rbp)	#, i
.L14:
# main.c:126:         for (i = 0; i < PARTICLE_CT; i++) {
	cmpl	$255, -140(%rbp)	#, i
	jle	.L21	#,
# main.c:177:         SDL_SetRenderDrawColor(renderer, 0, 0, 0, 0);
	movq	-112(%rbp), %rax	# renderer, tmp282
	movl	$0, %r8d	#,
	movl	$0, %ecx	#,
	movl	$0, %edx	#,
	movl	$0, %esi	#,
	movq	%rax, %rdi	# tmp282,
	call	SDL_SetRenderDrawColor@PLT	#
# main.c:178:         SDL_RenderClear(renderer);
	movq	-112(%rbp), %rax	# renderer, tmp283
	movq	%rax, %rdi	# tmp283,
	call	SDL_RenderClear@PLT	#
# main.c:182:         SDL_SetRenderDrawColor(renderer, 0, 255, 50, 255);
	movq	-112(%rbp), %rax	# renderer, tmp284
	movl	$255, %r8d	#,
	movl	$50, %ecx	#,
	movl	$255, %edx	#,
	movl	$0, %esi	#,
	movq	%rax, %rdi	# tmp284,
	call	SDL_SetRenderDrawColor@PLT	#
# main.c:186:         for (i = 0; i < PARTICLE_CT; i++) {
	movl	$0, -140(%rbp)	#, i
	jmp	.L22	#
.L23:
# main.c:190:                 particles[i]->y_pos
	movl	-140(%rbp), %eax	# i, tmp285
	cltq
	leaq	0(,%rax,8), %rdx	#, _107
	movq	-96(%rbp), %rax	# particles, tmp286
	addq	%rdx, %rax	# _107, _108
	movq	(%rax), %rax	# *_108, _109
	movss	4(%rax), %xmm0	# _109->y_pos, _110
# main.c:187:             SDL_RenderDrawPoint(
	cvttss2si	%xmm0, %edx	# _110, _111
# main.c:189:                 particles[i]->x_pos,
	movl	-140(%rbp), %eax	# i, tmp287
	cltq
	leaq	0(,%rax,8), %rcx	#, _113
	movq	-96(%rbp), %rax	# particles, tmp288
	addq	%rcx, %rax	# _113, _114
	movq	(%rax), %rax	# *_114, _115
	movss	(%rax), %xmm0	# _115->x_pos, _116
# main.c:187:             SDL_RenderDrawPoint(
	cvttss2si	%xmm0, %ecx	# _116, _117
	movq	-112(%rbp), %rax	# renderer, tmp289
	movl	%ecx, %esi	# _117,
	movq	%rax, %rdi	# tmp289,
	call	SDL_RenderDrawPoint@PLT	#
# main.c:186:         for (i = 0; i < PARTICLE_CT; i++) {
	addl	$1, -140(%rbp)	#, i
.L22:
# main.c:186:         for (i = 0; i < PARTICLE_CT; i++) {
	cmpl	$255, -140(%rbp)	#, i
	jle	.L23	#,
# main.c:194:         SDL_RenderPresent(renderer);
	movq	-112(%rbp), %rax	# renderer, tmp290
	movq	%rax, %rdi	# tmp290,
	call	SDL_RenderPresent@PLT	#
# main.c:197:         SDL_SetRenderDrawColor(renderer, 255, 10, 0, 255);
	movq	-112(%rbp), %rax	# renderer, tmp291
	movl	$255, %r8d	#,
	movl	$0, %ecx	#,
	movl	$10, %edx	#,
	movl	$255, %esi	#,
	movq	%rax, %rdi	# tmp291,
	call	SDL_SetRenderDrawColor@PLT	#
# main.c:199:         SDL_RenderDrawPoint(renderer, mouse_x, mouse_y);
	movl	-148(%rbp), %edx	# mouse_y, mouse_y.12_118
	movl	-152(%rbp), %ecx	# mouse_x, mouse_x.13_119
	movq	-112(%rbp), %rax	# renderer, tmp292
	movl	%ecx, %esi	# mouse_x.13_119,
	movq	%rax, %rdi	# tmp292,
	call	SDL_RenderDrawPoint@PLT	#
# main.c:200:         SDL_RenderDrawPoint(renderer, mouse_x-1, mouse_y);
	movl	-148(%rbp), %edx	# mouse_y, mouse_y.14_120
	movl	-152(%rbp), %eax	# mouse_x, mouse_x.15_121
	leal	-1(%rax), %ecx	#, _122
	movq	-112(%rbp), %rax	# renderer, tmp293
	movl	%ecx, %esi	# _122,
	movq	%rax, %rdi	# tmp293,
	call	SDL_RenderDrawPoint@PLT	#
# main.c:201:         SDL_RenderDrawPoint(renderer, mouse_x+1, mouse_y);
	movl	-148(%rbp), %edx	# mouse_y, mouse_y.16_123
	movl	-152(%rbp), %eax	# mouse_x, mouse_x.17_124
	leal	1(%rax), %ecx	#, _125
	movq	-112(%rbp), %rax	# renderer, tmp294
	movl	%ecx, %esi	# _125,
	movq	%rax, %rdi	# tmp294,
	call	SDL_RenderDrawPoint@PLT	#
# main.c:202:         SDL_RenderDrawPoint(renderer, mouse_x, mouse_y-1);
	movl	-148(%rbp), %eax	# mouse_y, mouse_y.18_126
	leal	-1(%rax), %edx	#, _127
	movl	-152(%rbp), %ecx	# mouse_x, mouse_x.19_128
	movq	-112(%rbp), %rax	# renderer, tmp295
	movl	%ecx, %esi	# mouse_x.19_128,
	movq	%rax, %rdi	# tmp295,
	call	SDL_RenderDrawPoint@PLT	#
# main.c:203:         SDL_RenderDrawPoint(renderer, mouse_x, mouse_y+1);
	movl	-148(%rbp), %eax	# mouse_y, mouse_y.20_129
	leal	1(%rax), %edx	#, _130
	movl	-152(%rbp), %ecx	# mouse_x, mouse_x.21_131
	movq	-112(%rbp), %rax	# renderer, tmp296
	movl	%ecx, %esi	# mouse_x.21_131,
	movq	%rax, %rdi	# tmp296,
	call	SDL_RenderDrawPoint@PLT	#
# main.c:205:         SDL_RenderPresent(renderer);
	movq	-112(%rbp), %rax	# renderer, tmp297
	movq	%rax, %rdi	# tmp297,
	call	SDL_RenderPresent@PLT	#
# main.c:208:         SDL_PollEvent(&event);
	leaq	-80(%rbp), %rax	#, tmp298
	movq	%rax, %rdi	# tmp298,
	call	SDL_PollEvent@PLT	#
# main.c:209:         switch (event.type) {
	movl	-80(%rbp), %eax	# event.type, _132
	cmpl	$768, %eax	#, _132
	je	.L24	#,
	cmpl	$769, %eax	#, _132
	je	.L9	#,
	cmpl	$256, %eax	#, _132
	je	.L26	#,
	jmp	.L9	#
.L26:
# main.c:211:                 window_open = 0;
	movl	$0, -144(%rbp)	#, window_open
# main.c:212:                 break;
	jmp	.L9	#
.L24:
# main.c:216:                 switch (event.key.keysym.sym) {
	movl	-60(%rbp), %eax	# event.key.keysym.sym, _133
	cmpl	$120, %eax	#, _133
	jne	.L27	#,
# main.c:218:                         printf("Closing the program.\n");
	leaq	.LC7(%rip), %rdi	#,
	call	puts@PLT	#
# main.c:219:                         window_open = 0;
	movl	$0, -144(%rbp)	#, window_open
# main.c:220:                         break;
	nop
.L27:
# main.c:222:                 break;
	nop
.L9:
# main.c:92:     while (window_open) {
	cmpl	$0, -144(%rbp)	#, window_open
	jne	.L29	#,
# main.c:227:     for (i = 0; i < PARTICLE_CT; i++) {
	movl	$0, -140(%rbp)	#, i
	jmp	.L30	#
.L31:
# main.c:228:         free_particle(particles[i]);
	movl	-140(%rbp), %eax	# i, tmp299
	cltq
	leaq	0(,%rax,8), %rdx	#, _135
	movq	-96(%rbp), %rax	# particles, tmp300
	addq	%rdx, %rax	# _135, _136
	movq	(%rax), %rax	# *_136, _137
	movq	%rax, %rdi	# _137,
	call	free_particle@PLT	#
# main.c:227:     for (i = 0; i < PARTICLE_CT; i++) {
	addl	$1, -140(%rbp)	#, i
.L30:
# main.c:227:     for (i = 0; i < PARTICLE_CT; i++) {
	cmpl	$255, -140(%rbp)	#, i
	jle	.L31	#,
# main.c:231:     free_particle(mouse_particle);
	movq	-104(%rbp), %rax	# mouse_particle, tmp301
	movq	%rax, %rdi	# tmp301,
	call	free_particle@PLT	#
# main.c:232:     free(particles);
	movq	-96(%rbp), %rax	# particles, tmp302
	movq	%rax, %rdi	# tmp302,
	call	free@PLT	#
# main.c:233:     SDL_DestroyRenderer(renderer);
	movq	-112(%rbp), %rax	# renderer, tmp303
	movq	%rax, %rdi	# tmp303,
	call	SDL_DestroyRenderer@PLT	#
# main.c:234:     SDL_DestroyWindow(main_window);
	movq	-120(%rbp), %rax	# main_window, tmp304
	movq	%rax, %rdi	# tmp304,
	call	SDL_DestroyWindow@PLT	#
# main.c:235:     SDL_Quit();
	call	SDL_Quit@PLT	#
# main.c:236:     return 0;
	movl	$0, %eax	#, _153
.L32:
# main.c:237: }
	movq	-24(%rbp), %rbx	# D.27368, tmp307
	xorq	%fs:40, %rbx	#, tmp307
	je	.L33	#,
# main.c:237: }
	call	__stack_chk_fail@PLT	#
.L33:
	addq	$184, %rsp	#,
	popq	%rbx	#
	popq	%rbp	#
	.cfi_def_cfa 7, 8
	ret
	.cfi_endproc
.LFE3676:
	.size	main, .-main
	.section	.rodata
	.align 8
.LC4:
	.long	0
	.long	1077149696
	.align 8
.LC5:
	.long	0
	.long	1080623104
	.align 4
.LC6:
	.long	1069547520
	.ident	"GCC: (Ubuntu 7.4.0-1ubuntu1~18.04.1) 7.4.0"
	.section	.note.GNU-stack,"",@progbits
