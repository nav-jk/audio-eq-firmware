#include "filter.h"
#include <math.h>

void filter_init(PARAMS* filt, float coeff[6])
{
    // filt->wc: 2π * fc / fs (digital rad/sample)
    // filt->wbw: 2π * BW_Hz (analog rad/s)
    // filt->T: 1/fs

    float wcd = (2.0f / filt->T) * tanf(filt->wc / 2.0f); // pre-warp
    float q   = wcd / filt->wbw;
    float wt  = wcd * filt->T;
    float wt2 = wt * wt;

    coeff[0] = 4.0f + ((2.0f * filt->g) / q) * wt + wt2;
    coeff[1] = 2.0f * wt2 - 8.0f;
    coeff[2] = 4.0f - ((2.0f * filt->g) / q) * wt + wt2;
    coeff[3] = 4.0f + (2.0f / q) * wt + wt2;
    coeff[4] = -(2.0f * wt2 - 8.0f);
    coeff[5] = -(4.0f - (2.0f / q) * wt + wt2);
}

float filter_update(float coeff[6],
                    float input_buffer[3],
                    float output_buffer[3])
{
    float out = (1.0f / coeff[3]) * (
        coeff[0] * input_buffer[0] +
        coeff[1] * input_buffer[1] +
        coeff[2] * input_buffer[2] +
        coeff[4] * output_buffer[1] +
        coeff[5] * output_buffer[2]
    );

    // shift histories
    input_buffer[2]  = input_buffer[1];
    input_buffer[1]  = input_buffer[0];

    output_buffer[2] = output_buffer[1];
    output_buffer[1] = out;

    output_buffer[0] = out;
    return out;
}

void buffer_update(float sample, float input_buffer[3])
{
    input_buffer[0] = sample;
}
