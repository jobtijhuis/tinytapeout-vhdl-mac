library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity simple_multiplier is
    port (
        io_in   : in std_logic_vector(7 downto 0);
        io_out  : out std_logic_vector(7 downto 0)
    );
end entity simple_multiplier;

architecture rtl of simple_multiplier is
    
    signal a_in  : std_logic_vector(3 downto 0);
    signal b_in  : std_logic_vector(3 downto 0);
    signal c_out : std_logic_vector(7 downto 0);

begin

    a_in <= io_in(3 downto 0);
    b_in <= io_in(7 downto 4);

    c_out <= std_logic_vector(unsigned(a_in) * unsigned(b_in));

    io_out <= c_out;
    
end architecture rtl;
