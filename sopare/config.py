#########################################################
# Stream prep and silence configuration options #########
#########################################################

# Read chunk size
CHUNK = 512

# Sample rate
SAMPLE_RATE = 44100

# Volume threshold when audio processing starts
THRESHOLD = 300

# Silence time in seconds when analysis is called
MAX_SILENCE_AFTER_START = 3

# Time in seconds after the analysis is forced
MAX_TIME = 5

# Counter to stop processing and prepare more data
# Should be > LONG_SILENCE
SILENCE_COUNTER = 100

# Tokenizer values to detect a new token
TOKEN_HIGH = 440
SILENCE = 5
# Start the analysis after reaching LONG_SILENCE
LONG_SILENCE = 60



#########################################################
# Characteristic configuration options ##################
#########################################################

# Steps boil down the data into smaller chunks of data.
# Smaller steps mean more precision but require
# normally more learned entries in the dictionary.
# Progressive value is used if you want to pack not
# so relevant frequencies
PROGRESSIVE_FACTOR = 0
START_PROGRESSIVE_FACTOR = 8000
MIN_PROGRESSIVE_STEP = 100
MAX_PROGRESSIVE_STEP = 100

# Specifies freq ranges that are kept for further
# analysis. Freq outside of the ranges are set to zero.
# Human language can be found between 20 and 5000.
LOW_FREQ = 20
HIGH_FREQ = 5000

# Make use of Hann window function
HANNING = True

# Minimal FFT length for consideration
# Default: 12
MIN_FFT_LEN = 12

# Minimal PEAKS length for consideration
# Default: 15
MIN_PEAKS_LEN = 15

# Minimal FFT max. value for consideration
# Default: 5000
MIN_FFT_MAX = 5000

# Min. adaptive value to create a characteristic
# Default: TDB
MIN_ADAPTING = 5000

# Range factor for peaks
PEAK_FACTOR = 3

#########################################################
# Compare configuration options #########################
#########################################################

# Number of tokens to identify the beginning of a word
COMPARE_START_TOKENS = 2

# Min. value for potential beginning of a word
MARGINAL_VALUE = 0.3

# Minimal similarity across all comparison to
# identify a complete word across all tokens
MIN_CROSS_SIMILARITY = 0.6

# Calculation basis for token/word comparison
SIMILARITY_PEAKS = 0.3
SIMILARITY_HEIGHT = 0.6
SIMILARITY_DOMINANT_FREQUENCY = 0.1
