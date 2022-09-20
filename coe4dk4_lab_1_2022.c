
/*
 *
 * Simulation of Single Server Queueing System
 * 
 * Copyright (C) 2014 Terence D. Todd Hamilton, Ontario, CANADA,
 * todd@mcmaster.ca
 * 
 * This program is free software; you can redistribute it and/or modify it under
 * the terms of the GNU General Public License as published by the Free Software
 * Foundation; either version 3 of the License, or (at your option) any later
 * version.
 * 
 * This program is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
 * details.
 * 
 * You should have received a copy of the GNU General Public License along with
 * this program.  If not, see <http://www.gnu.org/licenses/>.
 * 
 */

/*******************************************************************************/

#include <stdio.h>
#include "simlib.h"

/*******************************************************************************/

/*
 * Simulation Parameters
 */

#define RANDOM_SEED 5259140
#define NUMBER_TO_SERVE 50e6

#define SERVICE_TIME 30
#define ARRIVAL_RATE (1.0/SERVICE_TIME)

#define BLIP_RATE 10000

#define RUNS_PER_ARRIVAL_RATE 3

#define ARRAY_SIZE(x) (sizeof(x) / sizeof(x[0]))
/*******************************************************************************/

/*
 * main() uses various simulation parameters and creates a clock variable to
 * simulate real time. A loop repeatedly determines if the next event to occur
 * is a customer arrival or customer departure. In either case the state of the
 * system is updated and statistics are collected before the next
 * iteration. When it finally reaches NUMBER_TO_SERVE customers, the program
 * outputs some statistics such as mean delay.
 */

int main()
{
    /* Initalize file pointer */
    FILE * pSave;
    pSave  = fopen("data50_service_time30.txt", "w");
    /* Iterating through different RANDOM_SEED */
    int random_values[RUNS_PER_ARRIVAL_RATE] = {400191540, 400175089, 400186733};

    /* Generate random values */
    for (int i = 3; i < RUNS_PER_ARRIVAL_RATE; i++)
    {
        random_values[i] = random_values[i % 3] + i;
    }
    float arrival_rates[] = {ARRIVAL_RATE, ARRIVAL_RATE-0.001, ARRIVAL_RATE-0.005, ARRIVAL_RATE-0.01, ARRIVAL_RATE-0.03};
    /* Runs for each different arrivate_rate */
    for (int rate = 0; rate < ARRAY_SIZE(arrival_rates); rate++)
    {
        /*  Runs for differnent random seeds*/
        for (int seed = 0; seed < RUNS_PER_ARRIVAL_RATE; seed++)
        {
            double clock = 0; /* Clock keeps track of simulation time. */

            /* System state variables. */
            int number_in_system = 0;
            double next_arrival_time = 0;
            double next_departure_time = 0;

            /* Data collection variables. */
            long int total_served = 0;
            long int total_arrived = 0;

            double total_busy_time = 0;
            double integral_of_n = 0;
            double last_event_time = 0;

            random_generator_initialize(random_values[seed]);
            /* Set the seed of the random number generator. */

            /* Process customers until we are finished. */
            while (total_served < NUMBER_TO_SERVE) {

                /* Test if the next event is a customer arrival or departure. */
                if(number_in_system == 0 || next_arrival_time < next_departure_time) {

                    /*
                        * A new arrival is occurring.
                        */

                    clock = next_arrival_time;
                    next_arrival_time = clock + exponential_generator((double) 1/arrival_rates[rate]);

                    /* Update our statistics. */
                    integral_of_n += number_in_system * (clock - last_event_time);
                    last_event_time = clock;

                    number_in_system++;
                    total_arrived++;

                    /* If this customer has arrived to an empty system, start its
                    service right away. */
                    if(number_in_system == 1) next_departure_time = clock + SERVICE_TIME;

                }

                else
                {
                    /*
                        * A customer departure is occuring. 
                        */

                    clock = next_departure_time;

                    /* Update our statistics. */
                    integral_of_n += number_in_system * (clock - last_event_time);
                    last_event_time = clock;

                    number_in_system--;
                    total_served++;
                    total_busy_time += SERVICE_TIME;

                    /* 
                        * If there are other customers waiting, start one in service
                        * right away.
                        */

                    if(number_in_system > 0) next_departure_time = clock + SERVICE_TIME;

                    /* 
                        * Every so often, print an activity message to show we are active. 
                        */

                    // if (total_served % BLIP_RATE == 0)
                        // printf("Customers served = %ld (Total arrived = %ld)\r", total_served, total_arrived);
                }
            }

            /* Output final results. */
            double utilization = total_busy_time/clock;
            double fractionServed = (double) total_served/total_arrived;
            double meanNumberInSystem = integral_of_n/clock;
            double meanDelay = integral_of_n/total_served;
            printf("\nUtilization = %f\n", utilization);
            // printf("Fraction served = %f\n", fractionServed);
            // printf("Mean number in system = %f\n", meanNumberInSystem);
            // printf("Mean delay = %f\n", meanDelay);

            fprintf(pSave, "%d, %f, %f, %f, %f, %f\n", random_values[seed], arrival_rates[rate], utilization, fractionServed, meanNumberInSystem, meanDelay);
        }
        // fprintf(pSave,"Finished %d runs for arrival rate = %f\n", RUNS_PER_ARRIVAL_RATE, arrival_rates[rate]);
    }


    /* Halt the program before exiting. */
    printf("Hit Enter to finish ... \n");
    fclose(pSave);
    getchar(); 
    
    return 0;

}






