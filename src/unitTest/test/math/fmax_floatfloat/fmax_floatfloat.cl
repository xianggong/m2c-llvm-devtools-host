// Auto generated kernel

__kernel void fmax_floatfloat(__global float *src_0, __global float *src_1, __global float* dst)
{
	int gid = get_global_id(0);
	dst[gid] = fmax(src_0[gid], src_1[gid]);
}
