import argparse 
def process_command():
    parser = argparse.ArgumentParser()
    parser.add_argument('--foo', help='foo help')
    parser.add_argument('--text', '-t', default="park",type=str, required=False, help='Text for program')
    parser.add_argument('--int', '-i', default=0,type=int, required=False, help='I for program',nargs='+')
    parser.add_argument('--tuples', '-tu', default=None,type=tuple, required=False, help='tuple for program')
    return parser.parse_args()

def tuple_to_in(tuples):
    sum=0
    print(tuples)
    for i in tuples:
        sum*=10
        sum+=int(i)
    return sum
    
if __name__ == '__main__':
    args = process_command()
    if(args.tuples!=None):
         print(tuple_to_in(args.tuples))
