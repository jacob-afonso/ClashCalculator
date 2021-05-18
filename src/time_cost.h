#include <string>
#include <vector>

using namespace std;

typedef struct InUgLine{
    string lvl_str;
    string ug_str;
    string cost_str;
    string time_str;
    string amt_str;
} InUgLine;

typedef struct UgLine{
    string ug;
    int lvl;
    int amt;
} UgLine;

/**
 * Helper function to take the integer days and hours
 * and convert them to string form: XdXh
 */
string time_int_to_string(int days, int hours);

/**
 * Takes in days and hours and a decimal % builder reduction
 * Will reduce the time by the factor and return the result
 */
double reduce_time(int days, int hours, double factor);

/**
 * Helper function of reduce_time_str
 * Takes in the string and converts to days and hours as doubles
 * .first is days, .second is hours
 */
pair<double, double> time_str_to_double(string otime);

/**
 * Takes in the original time string format: XdXh
 * calls helper functions to perform the reduction
 * returns the reduced time as a double in all hours: (X-(X*factor))h
 */ 
double reduce_time_str(string otime, double factor);

/**
 * Take in the original cost and decimal %builder reduction
 * return the cost reduced by the factor
 */
int reduce_cost(int o_cost, double factor);

/**
 * Reads from input file each line into a InUgLine struct.
 * Converts this struct to correct values in UgLine struct. 
 * Returns a vector with 1 entriy being 1 line of the input file.
 */
vector<UgLine> read_input_file(string fname);

/**
 * Function to perform the main work of the program
 * takes in filename, number of builders, and factors
 * and outputs the total times and costs.
 */
void getvals(string fname, string th, int builders, double factor);