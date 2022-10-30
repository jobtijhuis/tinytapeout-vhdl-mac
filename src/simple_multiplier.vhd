library IEEE;
use IEEE.std_logic_1164.all;
use IEEE.numeric_std.all;

entity simple_multiplier is
    port (
        a_in    : in std_logic_vector(2 downto 0);
        b_in    : in std_logic_vector(2 downto 0);
        c_out   : out std_logic_vector(5 downto 0)
    );
end entity simple_multiplier;

architecture rtl of simple_multiplier is
    
begin
    
    c_out <= std_logic_vector(unsigned(a_in) * unsigned(b_in));
    
end architecture rtl;
