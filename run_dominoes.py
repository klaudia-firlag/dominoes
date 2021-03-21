import argparse


class Dominoes:
    @staticmethod
    def forward(in_sequence: str, num_iter: int = 1) -> str:
        return in_sequence

    @staticmethod
    def backward(in_sequence: str, num_iter: int = 1) -> str:
        return in_sequence


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--in_sequence', type=str, required=True,
                        help='String containing input sequence of dominoes')
    parser.add_argument('--num_iter', type=int, default=1,
                        help='Number of iterations to perform on the input dominoes sequence')
    parser.add_argument('--backward', action='store_true',
                        help='A flag for performing backward iterations')
    args = parser.parse_args()

    dominoes = Dominoes()
    if args.backward:
        result = dominoes.backward(args.in_sequence, args.num_iter)
    else:
        result = dominoes.backward(args.in_sequence, args.num_iter)

    print(f'Results after {args.num_iter}:'
          f'\tInput string:  {args.in_sequence}\n'
          f'\tOutput string: {args.result}')
