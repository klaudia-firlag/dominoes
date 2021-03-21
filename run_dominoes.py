import argparse
import re

DOMINOES_POSITIONS = ['/', '|', '\\']


class Dominoes:
    @staticmethod
    def assert_inputs_correct(in_string: str, num_iter: int):
        assert len(in_string) > 1, f'Input sequence too short ({len(in_string)} characters). ' \
                                   f'Required at least 2 characters'
        assert all(char in DOMINOES_POSITIONS for char in in_string), f'Invalid input sequence. ' \
                                                                      f'All characters must be from the following ' \
                                                                      f'list: {DOMINOES_POSITIONS}'

        assert num_iter > -1, f'num_iter must be zero or a positive number'

    def forward(self, in_string: str, num_iter: int = 1) -> str:
        self.assert_inputs_correct(in_string, num_iter)
        out_str = in_string

        for _ in range(num_iter):
            if in_string[:2] == '|\\':
                out_str = '\\' + out_str[1:]

            if in_string[-2:] == '/|':
                out_str = out_str[:-1] + '/'

            for found_pipe in re.finditer('\|', in_string[1:-1]):
                pipe_idx = found_pipe.regs[0][0] + 1  # + 1 to accommodate for char shift in in_string[1:-1]
                substring = in_string[pipe_idx - 1:pipe_idx + 2]

                if substring in ['/||', '/|/']:
                    out_str = out_str[:pipe_idx] + '/' + out_str[pipe_idx + 1:]
                elif substring in ['||\\', '\\|\\']:
                    out_str = out_str[:pipe_idx] + '\\' + out_str[pipe_idx + 1:]

            in_string = out_str

        return out_str

    @staticmethod
    def backward(in_string: str, num_iter: int = 1) -> str:
        if num_iter == 0:
            return in_string

        return in_string


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
        result = dominoes.forward(args.in_sequence, args.num_iter)

    print('success')
    print(f'Results after {args.num_iter} iterations:\n'
          f'\tInput string:  {args.in_sequence}\n'
          f'\tOutput string: {result}')
