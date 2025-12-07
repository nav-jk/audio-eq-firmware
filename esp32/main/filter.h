#pragma once
#include <stdint.h>

typedef struct filter_params {
    float g;    // gain
    float wc;   // digital center freq (rad/sample)
    float wbw;  // analog bandwidth (rad/s)
    float T;    // sampling period (s)
} PARAMS;

void filter_init(PARAMS* filt, float coeff[6]);

float filter_update(float coeff[6],
                    float input_buffer[3],
                    float output_buffer[3]);

void buffer_update(float sample, float input_buffer[3]);
